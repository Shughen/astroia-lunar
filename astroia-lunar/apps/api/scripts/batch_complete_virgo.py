"""Batch complet: Virgo - 144 interprétations (12 maisons × 12 ascendants)"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    {
        'moon_sign': 'Virgo',
        'moon_house': 1,
        'lunar_ascendant': 'Aries',
        'interpretation': '''**Ton mois en un mot : Analyse et action**

Ta Lune en Vierge en Maison 1 analyse ton image, ton corps, ta présentation au monde avec minutie. L'Ascendant Aries fonce : action immédiate. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 1 — Identité personnelle. Tu veux te perfectionner, te montrer impeccable, optimiser qui tu es. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aries te pousse à fonce dans ce domaine. Action immédiate. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Aries crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton image, ton corps, ta présentation au monde.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 1,
        'lunar_ascendant': 'Taurus',
        'interpretation': '''**Ton mois en un mot : Perfectionnisme ancré**

Ta Lune en Vierge en Maison 1 analyse ton image, ton corps, ta présentation au monde avec minutie. L'Ascendant Taurus ancre : stabilité progressive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 1 — Identité personnelle. Tu veux te perfectionner, te montrer impeccable, optimiser qui tu es. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Taurus te pousse à ancre dans ce domaine. Stabilité progressive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : patience concrète. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton image, ton corps, ta présentation au monde.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 1,
        'lunar_ascendant': 'Gemini',
        'interpretation': '''**Ton mois en un mot : Analyse et curiosité**

Ta Lune en Vierge en Maison 1 analyse ton image, ton corps, ta présentation au monde avec minutie. L'Ascendant Gemini explore : curiosité multiple. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 1 — Identité personnelle. Tu veux te perfectionner, te montrer impeccable, optimiser qui tu es. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Gemini te pousse à explore dans ce domaine. Curiosité multiple. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Gemini multiplie les observations sans toujours agir. Dispersion intellectuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton image, ton corps, ta présentation au monde.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 1,
        'lunar_ascendant': 'Cancer',
        'interpretation': '''**Ton mois en un mot : Analyse et sensibilité**

Ta Lune en Vierge en Maison 1 analyse ton image, ton corps, ta présentation au monde avec minutie. L'Ascendant Cancer ressens : sensibilité profonde. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 1 — Identité personnelle. Tu veux te perfectionner, te montrer impeccable, optimiser qui tu es. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Cancer te pousse à ressens dans ce domaine. Sensibilité profonde. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Cancer complique l'analyse Vierge. Besoin de sécurité émotionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton image, ton corps, ta présentation au monde.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 1,
        'lunar_ascendant': 'Leo',
        'interpretation': '''**Ton mois en un mot : Analyse et fierté**

Ta Lune en Vierge en Maison 1 analyse ton image, ton corps, ta présentation au monde avec minutie. L'Ascendant Leo brille : fierté visible. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 1 — Identité personnelle. Tu veux te perfectionner, te montrer impeccable, optimiser qui tu es. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Leo te pousse à brille dans ce domaine. Fierté visible. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Leo crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton image, ton corps, ta présentation au monde.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 1,
        'lunar_ascendant': 'Virgo',
        'interpretation': '''**Ton mois en un mot : Triple analyse identité personnelle**

Ta Lune en Vierge en Maison 1 analyse ton image, ton corps, ta présentation au monde avec minutie. Triple Vierge : le perfectionnisme atteint son paroxysme. Chaque détail est scruté, optimisé, amélioré sans relâche.

**Domaine activé** : Maison 1 — Identité personnelle. Tu veux te perfectionner, te montrer impeccable, optimiser qui tu es. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Virgo te pousse à analyse dans ce domaine. Perfectionnisme total. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : contrôle minutieux. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton image, ton corps, ta présentation au monde.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 1,
        'lunar_ascendant': 'Libra',
        'interpretation': '''**Ton mois en un mot : Analyse et recherche**

Ta Lune en Vierge en Maison 1 analyse ton image, ton corps, ta présentation au monde avec minutie. L'Ascendant Libra équilibre : recherche d'harmonie. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 1 — Identité personnelle. Tu veux te perfectionner, te montrer impeccable, optimiser qui tu es. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Libra te pousse à équilibre dans ce domaine. Recherche d'harmonie. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Libra multiplie les observations sans toujours agir. Indécision élégante. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton image, ton corps, ta présentation au monde.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 1,
        'lunar_ascendant': 'Scorpio',
        'interpretation': '''**Ton mois en un mot : Perfection intense**

Ta Lune en Vierge en Maison 1 analyse ton image, ton corps, ta présentation au monde avec minutie. L'Ascendant Scorpio transforme : intensité émotionnelle. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 1 — Identité personnelle. Tu veux te perfectionner, te montrer impeccable, optimiser qui tu es. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Scorpio te pousse à transforme dans ce domaine. Intensité émotionnelle. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Scorpio complique l'analyse Vierge. Profondeur obsessionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton image, ton corps, ta présentation au monde.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 1,
        'lunar_ascendant': 'Sagittarius',
        'interpretation': '''**Ton mois en un mot : Analyse et vision**

Ta Lune en Vierge en Maison 1 analyse ton image, ton corps, ta présentation au monde avec minutie. L'Ascendant Sagittarius explore : vision philosophique. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 1 — Identité personnelle. Tu veux te perfectionner, te montrer impeccable, optimiser qui tu es. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Sagittarius te pousse à explore dans ce domaine. Vision philosophique. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Sagittarius crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton image, ton corps, ta présentation au monde.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 1,
        'lunar_ascendant': 'Capricorn',
        'interpretation': '''**Ton mois en un mot : Excellence structurée**

Ta Lune en Vierge en Maison 1 analyse ton image, ton corps, ta présentation au monde avec minutie. L'Ascendant Capricorn construit : ambition structurée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 1 — Identité personnelle. Tu veux te perfectionner, te montrer impeccable, optimiser qui tu es. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Capricorn te pousse à construit dans ce domaine. Ambition structurée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : discipline à long terme. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton image, ton corps, ta présentation au monde.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 1,
        'lunar_ascendant': 'Aquarius',
        'interpretation': '''**Ton mois en un mot : Analyse et originalité**

Ta Lune en Vierge en Maison 1 analyse ton image, ton corps, ta présentation au monde avec minutie. L'Ascendant Aquarius innove : originalité détachée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 1 — Identité personnelle. Tu veux te perfectionner, te montrer impeccable, optimiser qui tu es. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aquarius te pousse à innove dans ce domaine. Originalité détachée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Aquarius multiplie les observations sans toujours agir. Expérimentation conceptuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton image, ton corps, ta présentation au monde.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 1,
        'lunar_ascendant': 'Pisces',
        'interpretation': '''**Ton mois en un mot : Ordre et chaos**

Ta Lune en Vierge en Maison 1 analyse ton image, ton corps, ta présentation au monde avec minutie. L'Ascendant Pisces dissout : fluidité intuitive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 1 — Identité personnelle. Tu veux te perfectionner, te montrer impeccable, optimiser qui tu es. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Pisces te pousse à dissout dans ce domaine. Fluidité intuitive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Pisces complique l'analyse Vierge. Fusion compassionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton image, ton corps, ta présentation au monde.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 2,
        'lunar_ascendant': 'Aries',
        'interpretation': '''**Ton mois en un mot : Analyse et action**

Ta Lune en Vierge en Maison 2 analyse tes finances, tes possessions, ta valeur matérielle avec minutie. L'Ascendant Aries fonce : action immédiate. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 2 — Ressources et sécurité. Tu veux gérer méthodiquement, économiser efficacement, optimiser tes revenus. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aries te pousse à fonce dans ce domaine. Action immédiate. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Aries crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes finances, tes possessions, ta valeur matérielle.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 2,
        'lunar_ascendant': 'Taurus',
        'interpretation': '''**Ton mois en un mot : Perfectionnisme ancré**

Ta Lune en Vierge en Maison 2 analyse tes finances, tes possessions, ta valeur matérielle avec minutie. L'Ascendant Taurus ancre : stabilité progressive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 2 — Ressources et sécurité. Tu veux gérer méthodiquement, économiser efficacement, optimiser tes revenus. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Taurus te pousse à ancre dans ce domaine. Stabilité progressive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : patience concrète. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes finances, tes possessions, ta valeur matérielle.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 2,
        'lunar_ascendant': 'Gemini',
        'interpretation': '''**Ton mois en un mot : Analyse et curiosité**

Ta Lune en Vierge en Maison 2 analyse tes finances, tes possessions, ta valeur matérielle avec minutie. L'Ascendant Gemini explore : curiosité multiple. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 2 — Ressources et sécurité. Tu veux gérer méthodiquement, économiser efficacement, optimiser tes revenus. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Gemini te pousse à explore dans ce domaine. Curiosité multiple. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Gemini multiplie les observations sans toujours agir. Dispersion intellectuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes finances, tes possessions, ta valeur matérielle.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 2,
        'lunar_ascendant': 'Cancer',
        'interpretation': '''**Ton mois en un mot : Analyse et sensibilité**

Ta Lune en Vierge en Maison 2 analyse tes finances, tes possessions, ta valeur matérielle avec minutie. L'Ascendant Cancer ressens : sensibilité profonde. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 2 — Ressources et sécurité. Tu veux gérer méthodiquement, économiser efficacement, optimiser tes revenus. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Cancer te pousse à ressens dans ce domaine. Sensibilité profonde. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Cancer complique l'analyse Vierge. Besoin de sécurité émotionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes finances, tes possessions, ta valeur matérielle.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 2,
        'lunar_ascendant': 'Leo',
        'interpretation': '''**Ton mois en un mot : Analyse et fierté**

Ta Lune en Vierge en Maison 2 analyse tes finances, tes possessions, ta valeur matérielle avec minutie. L'Ascendant Leo brille : fierté visible. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 2 — Ressources et sécurité. Tu veux gérer méthodiquement, économiser efficacement, optimiser tes revenus. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Leo te pousse à brille dans ce domaine. Fierté visible. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Leo crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes finances, tes possessions, ta valeur matérielle.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 2,
        'lunar_ascendant': 'Virgo',
        'interpretation': '''**Ton mois en un mot : Triple analyse ressources et sécurité**

Ta Lune en Vierge en Maison 2 analyse tes finances, tes possessions, ta valeur matérielle avec minutie. Triple Vierge : le perfectionnisme atteint son paroxysme. Chaque détail est scruté, optimisé, amélioré sans relâche.

**Domaine activé** : Maison 2 — Ressources et sécurité. Tu veux gérer méthodiquement, économiser efficacement, optimiser tes revenus. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Virgo te pousse à analyse dans ce domaine. Perfectionnisme total. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : contrôle minutieux. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes finances, tes possessions, ta valeur matérielle.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 2,
        'lunar_ascendant': 'Libra',
        'interpretation': '''**Ton mois en un mot : Analyse et recherche**

Ta Lune en Vierge en Maison 2 analyse tes finances, tes possessions, ta valeur matérielle avec minutie. L'Ascendant Libra équilibre : recherche d'harmonie. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 2 — Ressources et sécurité. Tu veux gérer méthodiquement, économiser efficacement, optimiser tes revenus. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Libra te pousse à équilibre dans ce domaine. Recherche d'harmonie. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Libra multiplie les observations sans toujours agir. Indécision élégante. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes finances, tes possessions, ta valeur matérielle.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 2,
        'lunar_ascendant': 'Scorpio',
        'interpretation': '''**Ton mois en un mot : Perfection intense**

Ta Lune en Vierge en Maison 2 analyse tes finances, tes possessions, ta valeur matérielle avec minutie. L'Ascendant Scorpio transforme : intensité émotionnelle. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 2 — Ressources et sécurité. Tu veux gérer méthodiquement, économiser efficacement, optimiser tes revenus. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Scorpio te pousse à transforme dans ce domaine. Intensité émotionnelle. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Scorpio complique l'analyse Vierge. Profondeur obsessionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes finances, tes possessions, ta valeur matérielle.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 2,
        'lunar_ascendant': 'Sagittarius',
        'interpretation': '''**Ton mois en un mot : Analyse et vision**

Ta Lune en Vierge en Maison 2 analyse tes finances, tes possessions, ta valeur matérielle avec minutie. L'Ascendant Sagittarius explore : vision philosophique. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 2 — Ressources et sécurité. Tu veux gérer méthodiquement, économiser efficacement, optimiser tes revenus. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Sagittarius te pousse à explore dans ce domaine. Vision philosophique. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Sagittarius crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes finances, tes possessions, ta valeur matérielle.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 2,
        'lunar_ascendant': 'Capricorn',
        'interpretation': '''**Ton mois en un mot : Excellence structurée**

Ta Lune en Vierge en Maison 2 analyse tes finances, tes possessions, ta valeur matérielle avec minutie. L'Ascendant Capricorn construit : ambition structurée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 2 — Ressources et sécurité. Tu veux gérer méthodiquement, économiser efficacement, optimiser tes revenus. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Capricorn te pousse à construit dans ce domaine. Ambition structurée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : discipline à long terme. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes finances, tes possessions, ta valeur matérielle.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 2,
        'lunar_ascendant': 'Aquarius',
        'interpretation': '''**Ton mois en un mot : Analyse et originalité**

Ta Lune en Vierge en Maison 2 analyse tes finances, tes possessions, ta valeur matérielle avec minutie. L'Ascendant Aquarius innove : originalité détachée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 2 — Ressources et sécurité. Tu veux gérer méthodiquement, économiser efficacement, optimiser tes revenus. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aquarius te pousse à innove dans ce domaine. Originalité détachée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Aquarius multiplie les observations sans toujours agir. Expérimentation conceptuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes finances, tes possessions, ta valeur matérielle.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 2,
        'lunar_ascendant': 'Pisces',
        'interpretation': '''**Ton mois en un mot : Ordre et chaos**

Ta Lune en Vierge en Maison 2 analyse tes finances, tes possessions, ta valeur matérielle avec minutie. L'Ascendant Pisces dissout : fluidité intuitive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 2 — Ressources et sécurité. Tu veux gérer méthodiquement, économiser efficacement, optimiser tes revenus. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Pisces te pousse à dissout dans ce domaine. Fluidité intuitive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Pisces complique l'analyse Vierge. Fusion compassionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes finances, tes possessions, ta valeur matérielle.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 3,
        'lunar_ascendant': 'Aries',
        'interpretation': '''**Ton mois en un mot : Analyse et action**

Ta Lune en Vierge en Maison 3 analyse tes échanges, tes mots, ton quotidien intellectuel avec minutie. L'Ascendant Aries fonce : action immédiate. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 3 — Communication et apprentissage. Tu veux communiquer précisément, apprendre méthodiquement, analyser les échanges. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aries te pousse à fonce dans ce domaine. Action immédiate. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Aries crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes échanges, tes mots, ton quotidien intellectuel.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 3,
        'lunar_ascendant': 'Taurus',
        'interpretation': '''**Ton mois en un mot : Perfectionnisme ancré**

Ta Lune en Vierge en Maison 3 analyse tes échanges, tes mots, ton quotidien intellectuel avec minutie. L'Ascendant Taurus ancre : stabilité progressive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 3 — Communication et apprentissage. Tu veux communiquer précisément, apprendre méthodiquement, analyser les échanges. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Taurus te pousse à ancre dans ce domaine. Stabilité progressive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : patience concrète. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes échanges, tes mots, ton quotidien intellectuel.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 3,
        'lunar_ascendant': 'Gemini',
        'interpretation': '''**Ton mois en un mot : Analyse et curiosité**

Ta Lune en Vierge en Maison 3 analyse tes échanges, tes mots, ton quotidien intellectuel avec minutie. L'Ascendant Gemini explore : curiosité multiple. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 3 — Communication et apprentissage. Tu veux communiquer précisément, apprendre méthodiquement, analyser les échanges. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Gemini te pousse à explore dans ce domaine. Curiosité multiple. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Gemini multiplie les observations sans toujours agir. Dispersion intellectuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes échanges, tes mots, ton quotidien intellectuel.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 3,
        'lunar_ascendant': 'Cancer',
        'interpretation': '''**Ton mois en un mot : Analyse et sensibilité**

Ta Lune en Vierge en Maison 3 analyse tes échanges, tes mots, ton quotidien intellectuel avec minutie. L'Ascendant Cancer ressens : sensibilité profonde. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 3 — Communication et apprentissage. Tu veux communiquer précisément, apprendre méthodiquement, analyser les échanges. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Cancer te pousse à ressens dans ce domaine. Sensibilité profonde. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Cancer complique l'analyse Vierge. Besoin de sécurité émotionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes échanges, tes mots, ton quotidien intellectuel.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 3,
        'lunar_ascendant': 'Leo',
        'interpretation': '''**Ton mois en un mot : Analyse et fierté**

Ta Lune en Vierge en Maison 3 analyse tes échanges, tes mots, ton quotidien intellectuel avec minutie. L'Ascendant Leo brille : fierté visible. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 3 — Communication et apprentissage. Tu veux communiquer précisément, apprendre méthodiquement, analyser les échanges. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Leo te pousse à brille dans ce domaine. Fierté visible. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Leo crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes échanges, tes mots, ton quotidien intellectuel.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 3,
        'lunar_ascendant': 'Virgo',
        'interpretation': '''**Ton mois en un mot : Triple analyse communication et apprentissage**

Ta Lune en Vierge en Maison 3 analyse tes échanges, tes mots, ton quotidien intellectuel avec minutie. Triple Vierge : le perfectionnisme atteint son paroxysme. Chaque détail est scruté, optimisé, amélioré sans relâche.

**Domaine activé** : Maison 3 — Communication et apprentissage. Tu veux communiquer précisément, apprendre méthodiquement, analyser les échanges. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Virgo te pousse à analyse dans ce domaine. Perfectionnisme total. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : contrôle minutieux. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes échanges, tes mots, ton quotidien intellectuel.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 3,
        'lunar_ascendant': 'Libra',
        'interpretation': '''**Ton mois en un mot : Analyse et recherche**

Ta Lune en Vierge en Maison 3 analyse tes échanges, tes mots, ton quotidien intellectuel avec minutie. L'Ascendant Libra équilibre : recherche d'harmonie. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 3 — Communication et apprentissage. Tu veux communiquer précisément, apprendre méthodiquement, analyser les échanges. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Libra te pousse à équilibre dans ce domaine. Recherche d'harmonie. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Libra multiplie les observations sans toujours agir. Indécision élégante. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes échanges, tes mots, ton quotidien intellectuel.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 3,
        'lunar_ascendant': 'Scorpio',
        'interpretation': '''**Ton mois en un mot : Perfection intense**

Ta Lune en Vierge en Maison 3 analyse tes échanges, tes mots, ton quotidien intellectuel avec minutie. L'Ascendant Scorpio transforme : intensité émotionnelle. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 3 — Communication et apprentissage. Tu veux communiquer précisément, apprendre méthodiquement, analyser les échanges. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Scorpio te pousse à transforme dans ce domaine. Intensité émotionnelle. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Scorpio complique l'analyse Vierge. Profondeur obsessionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes échanges, tes mots, ton quotidien intellectuel.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 3,
        'lunar_ascendant': 'Sagittarius',
        'interpretation': '''**Ton mois en un mot : Analyse et vision**

Ta Lune en Vierge en Maison 3 analyse tes échanges, tes mots, ton quotidien intellectuel avec minutie. L'Ascendant Sagittarius explore : vision philosophique. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 3 — Communication et apprentissage. Tu veux communiquer précisément, apprendre méthodiquement, analyser les échanges. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Sagittarius te pousse à explore dans ce domaine. Vision philosophique. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Sagittarius crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes échanges, tes mots, ton quotidien intellectuel.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 3,
        'lunar_ascendant': 'Capricorn',
        'interpretation': '''**Ton mois en un mot : Excellence structurée**

Ta Lune en Vierge en Maison 3 analyse tes échanges, tes mots, ton quotidien intellectuel avec minutie. L'Ascendant Capricorn construit : ambition structurée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 3 — Communication et apprentissage. Tu veux communiquer précisément, apprendre méthodiquement, analyser les échanges. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Capricorn te pousse à construit dans ce domaine. Ambition structurée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : discipline à long terme. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes échanges, tes mots, ton quotidien intellectuel.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 3,
        'lunar_ascendant': 'Aquarius',
        'interpretation': '''**Ton mois en un mot : Analyse et originalité**

Ta Lune en Vierge en Maison 3 analyse tes échanges, tes mots, ton quotidien intellectuel avec minutie. L'Ascendant Aquarius innove : originalité détachée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 3 — Communication et apprentissage. Tu veux communiquer précisément, apprendre méthodiquement, analyser les échanges. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aquarius te pousse à innove dans ce domaine. Originalité détachée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Aquarius multiplie les observations sans toujours agir. Expérimentation conceptuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes échanges, tes mots, ton quotidien intellectuel.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 3,
        'lunar_ascendant': 'Pisces',
        'interpretation': '''**Ton mois en un mot : Ordre et chaos**

Ta Lune en Vierge en Maison 3 analyse tes échanges, tes mots, ton quotidien intellectuel avec minutie. L'Ascendant Pisces dissout : fluidité intuitive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 3 — Communication et apprentissage. Tu veux communiquer précisément, apprendre méthodiquement, analyser les échanges. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Pisces te pousse à dissout dans ce domaine. Fluidité intuitive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Pisces complique l'analyse Vierge. Fusion compassionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes échanges, tes mots, ton quotidien intellectuel.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 4,
        'lunar_ascendant': 'Aries',
        'interpretation': '''**Ton mois en un mot : Analyse et action**

Ta Lune en Vierge en Maison 4 analyse ton chez-toi, ta famille, tes fondations émotionnelles avec minutie. L'Ascendant Aries fonce : action immédiate. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 4 — Foyer et racines. Tu veux organiser ton espace, trier ton passé, créer un refuge fonctionnel. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aries te pousse à fonce dans ce domaine. Action immédiate. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Aries crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton chez-toi, ta famille, tes fondations émotionnelles.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 4,
        'lunar_ascendant': 'Taurus',
        'interpretation': '''**Ton mois en un mot : Perfectionnisme ancré**

Ta Lune en Vierge en Maison 4 analyse ton chez-toi, ta famille, tes fondations émotionnelles avec minutie. L'Ascendant Taurus ancre : stabilité progressive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 4 — Foyer et racines. Tu veux organiser ton espace, trier ton passé, créer un refuge fonctionnel. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Taurus te pousse à ancre dans ce domaine. Stabilité progressive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : patience concrète. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton chez-toi, ta famille, tes fondations émotionnelles.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 4,
        'lunar_ascendant': 'Gemini',
        'interpretation': '''**Ton mois en un mot : Analyse et curiosité**

Ta Lune en Vierge en Maison 4 analyse ton chez-toi, ta famille, tes fondations émotionnelles avec minutie. L'Ascendant Gemini explore : curiosité multiple. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 4 — Foyer et racines. Tu veux organiser ton espace, trier ton passé, créer un refuge fonctionnel. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Gemini te pousse à explore dans ce domaine. Curiosité multiple. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Gemini multiplie les observations sans toujours agir. Dispersion intellectuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton chez-toi, ta famille, tes fondations émotionnelles.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 4,
        'lunar_ascendant': 'Cancer',
        'interpretation': '''**Ton mois en un mot : Analyse et sensibilité**

Ta Lune en Vierge en Maison 4 analyse ton chez-toi, ta famille, tes fondations émotionnelles avec minutie. L'Ascendant Cancer ressens : sensibilité profonde. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 4 — Foyer et racines. Tu veux organiser ton espace, trier ton passé, créer un refuge fonctionnel. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Cancer te pousse à ressens dans ce domaine. Sensibilité profonde. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Cancer complique l'analyse Vierge. Besoin de sécurité émotionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton chez-toi, ta famille, tes fondations émotionnelles.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 4,
        'lunar_ascendant': 'Leo',
        'interpretation': '''**Ton mois en un mot : Analyse et fierté**

Ta Lune en Vierge en Maison 4 analyse ton chez-toi, ta famille, tes fondations émotionnelles avec minutie. L'Ascendant Leo brille : fierté visible. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 4 — Foyer et racines. Tu veux organiser ton espace, trier ton passé, créer un refuge fonctionnel. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Leo te pousse à brille dans ce domaine. Fierté visible. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Leo crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton chez-toi, ta famille, tes fondations émotionnelles.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 4,
        'lunar_ascendant': 'Virgo',
        'interpretation': '''**Ton mois en un mot : Triple analyse foyer et racines**

Ta Lune en Vierge en Maison 4 analyse ton chez-toi, ta famille, tes fondations émotionnelles avec minutie. Triple Vierge : le perfectionnisme atteint son paroxysme. Chaque détail est scruté, optimisé, amélioré sans relâche.

**Domaine activé** : Maison 4 — Foyer et racines. Tu veux organiser ton espace, trier ton passé, créer un refuge fonctionnel. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Virgo te pousse à analyse dans ce domaine. Perfectionnisme total. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : contrôle minutieux. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton chez-toi, ta famille, tes fondations émotionnelles.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 4,
        'lunar_ascendant': 'Libra',
        'interpretation': '''**Ton mois en un mot : Analyse et recherche**

Ta Lune en Vierge en Maison 4 analyse ton chez-toi, ta famille, tes fondations émotionnelles avec minutie. L'Ascendant Libra équilibre : recherche d'harmonie. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 4 — Foyer et racines. Tu veux organiser ton espace, trier ton passé, créer un refuge fonctionnel. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Libra te pousse à équilibre dans ce domaine. Recherche d'harmonie. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Libra multiplie les observations sans toujours agir. Indécision élégante. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton chez-toi, ta famille, tes fondations émotionnelles.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 4,
        'lunar_ascendant': 'Scorpio',
        'interpretation': '''**Ton mois en un mot : Perfection intense**

Ta Lune en Vierge en Maison 4 analyse ton chez-toi, ta famille, tes fondations émotionnelles avec minutie. L'Ascendant Scorpio transforme : intensité émotionnelle. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 4 — Foyer et racines. Tu veux organiser ton espace, trier ton passé, créer un refuge fonctionnel. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Scorpio te pousse à transforme dans ce domaine. Intensité émotionnelle. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Scorpio complique l'analyse Vierge. Profondeur obsessionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton chez-toi, ta famille, tes fondations émotionnelles.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 4,
        'lunar_ascendant': 'Sagittarius',
        'interpretation': '''**Ton mois en un mot : Analyse et vision**

Ta Lune en Vierge en Maison 4 analyse ton chez-toi, ta famille, tes fondations émotionnelles avec minutie. L'Ascendant Sagittarius explore : vision philosophique. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 4 — Foyer et racines. Tu veux organiser ton espace, trier ton passé, créer un refuge fonctionnel. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Sagittarius te pousse à explore dans ce domaine. Vision philosophique. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Sagittarius crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton chez-toi, ta famille, tes fondations émotionnelles.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 4,
        'lunar_ascendant': 'Capricorn',
        'interpretation': '''**Ton mois en un mot : Excellence structurée**

Ta Lune en Vierge en Maison 4 analyse ton chez-toi, ta famille, tes fondations émotionnelles avec minutie. L'Ascendant Capricorn construit : ambition structurée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 4 — Foyer et racines. Tu veux organiser ton espace, trier ton passé, créer un refuge fonctionnel. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Capricorn te pousse à construit dans ce domaine. Ambition structurée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : discipline à long terme. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton chez-toi, ta famille, tes fondations émotionnelles.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 4,
        'lunar_ascendant': 'Aquarius',
        'interpretation': '''**Ton mois en un mot : Analyse et originalité**

Ta Lune en Vierge en Maison 4 analyse ton chez-toi, ta famille, tes fondations émotionnelles avec minutie. L'Ascendant Aquarius innove : originalité détachée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 4 — Foyer et racines. Tu veux organiser ton espace, trier ton passé, créer un refuge fonctionnel. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aquarius te pousse à innove dans ce domaine. Originalité détachée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Aquarius multiplie les observations sans toujours agir. Expérimentation conceptuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton chez-toi, ta famille, tes fondations émotionnelles.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 4,
        'lunar_ascendant': 'Pisces',
        'interpretation': '''**Ton mois en un mot : Ordre et chaos**

Ta Lune en Vierge en Maison 4 analyse ton chez-toi, ta famille, tes fondations émotionnelles avec minutie. L'Ascendant Pisces dissout : fluidité intuitive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 4 — Foyer et racines. Tu veux organiser ton espace, trier ton passé, créer un refuge fonctionnel. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Pisces te pousse à dissout dans ce domaine. Fluidité intuitive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Pisces complique l'analyse Vierge. Fusion compassionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton chez-toi, ta famille, tes fondations émotionnelles.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 5,
        'lunar_ascendant': 'Aries',
        'interpretation': '''**Ton mois en un mot : Analyse et action**

Ta Lune en Vierge en Maison 5 analyse tes créations, tes loisirs, tes romances avec minutie. L'Ascendant Aries fonce : action immédiate. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 5 — Créativité et plaisir. Tu veux créer avec méthode, perfectionner tes talents, analyser le plaisir. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aries te pousse à fonce dans ce domaine. Action immédiate. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Aries crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes créations, tes loisirs, tes romances.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 5,
        'lunar_ascendant': 'Taurus',
        'interpretation': '''**Ton mois en un mot : Perfectionnisme ancré**

Ta Lune en Vierge en Maison 5 analyse tes créations, tes loisirs, tes romances avec minutie. L'Ascendant Taurus ancre : stabilité progressive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 5 — Créativité et plaisir. Tu veux créer avec méthode, perfectionner tes talents, analyser le plaisir. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Taurus te pousse à ancre dans ce domaine. Stabilité progressive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : patience concrète. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes créations, tes loisirs, tes romances.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 5,
        'lunar_ascendant': 'Gemini',
        'interpretation': '''**Ton mois en un mot : Analyse et curiosité**

Ta Lune en Vierge en Maison 5 analyse tes créations, tes loisirs, tes romances avec minutie. L'Ascendant Gemini explore : curiosité multiple. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 5 — Créativité et plaisir. Tu veux créer avec méthode, perfectionner tes talents, analyser le plaisir. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Gemini te pousse à explore dans ce domaine. Curiosité multiple. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Gemini multiplie les observations sans toujours agir. Dispersion intellectuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes créations, tes loisirs, tes romances.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 5,
        'lunar_ascendant': 'Cancer',
        'interpretation': '''**Ton mois en un mot : Analyse et sensibilité**

Ta Lune en Vierge en Maison 5 analyse tes créations, tes loisirs, tes romances avec minutie. L'Ascendant Cancer ressens : sensibilité profonde. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 5 — Créativité et plaisir. Tu veux créer avec méthode, perfectionner tes talents, analyser le plaisir. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Cancer te pousse à ressens dans ce domaine. Sensibilité profonde. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Cancer complique l'analyse Vierge. Besoin de sécurité émotionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes créations, tes loisirs, tes romances.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 5,
        'lunar_ascendant': 'Leo',
        'interpretation': '''**Ton mois en un mot : Analyse et fierté**

Ta Lune en Vierge en Maison 5 analyse tes créations, tes loisirs, tes romances avec minutie. L'Ascendant Leo brille : fierté visible. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 5 — Créativité et plaisir. Tu veux créer avec méthode, perfectionner tes talents, analyser le plaisir. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Leo te pousse à brille dans ce domaine. Fierté visible. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Leo crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes créations, tes loisirs, tes romances.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 5,
        'lunar_ascendant': 'Virgo',
        'interpretation': '''**Ton mois en un mot : Triple analyse créativité et plaisir**

Ta Lune en Vierge en Maison 5 analyse tes créations, tes loisirs, tes romances avec minutie. Triple Vierge : le perfectionnisme atteint son paroxysme. Chaque détail est scruté, optimisé, amélioré sans relâche.

**Domaine activé** : Maison 5 — Créativité et plaisir. Tu veux créer avec méthode, perfectionner tes talents, analyser le plaisir. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Virgo te pousse à analyse dans ce domaine. Perfectionnisme total. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : contrôle minutieux. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes créations, tes loisirs, tes romances.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 5,
        'lunar_ascendant': 'Libra',
        'interpretation': '''**Ton mois en un mot : Analyse et recherche**

Ta Lune en Vierge en Maison 5 analyse tes créations, tes loisirs, tes romances avec minutie. L'Ascendant Libra équilibre : recherche d'harmonie. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 5 — Créativité et plaisir. Tu veux créer avec méthode, perfectionner tes talents, analyser le plaisir. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Libra te pousse à équilibre dans ce domaine. Recherche d'harmonie. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Libra multiplie les observations sans toujours agir. Indécision élégante. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes créations, tes loisirs, tes romances.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 5,
        'lunar_ascendant': 'Scorpio',
        'interpretation': '''**Ton mois en un mot : Perfection intense**

Ta Lune en Vierge en Maison 5 analyse tes créations, tes loisirs, tes romances avec minutie. L'Ascendant Scorpio transforme : intensité émotionnelle. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 5 — Créativité et plaisir. Tu veux créer avec méthode, perfectionner tes talents, analyser le plaisir. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Scorpio te pousse à transforme dans ce domaine. Intensité émotionnelle. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Scorpio complique l'analyse Vierge. Profondeur obsessionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes créations, tes loisirs, tes romances.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 5,
        'lunar_ascendant': 'Sagittarius',
        'interpretation': '''**Ton mois en un mot : Analyse et vision**

Ta Lune en Vierge en Maison 5 analyse tes créations, tes loisirs, tes romances avec minutie. L'Ascendant Sagittarius explore : vision philosophique. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 5 — Créativité et plaisir. Tu veux créer avec méthode, perfectionner tes talents, analyser le plaisir. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Sagittarius te pousse à explore dans ce domaine. Vision philosophique. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Sagittarius crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes créations, tes loisirs, tes romances.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 5,
        'lunar_ascendant': 'Capricorn',
        'interpretation': '''**Ton mois en un mot : Excellence structurée**

Ta Lune en Vierge en Maison 5 analyse tes créations, tes loisirs, tes romances avec minutie. L'Ascendant Capricorn construit : ambition structurée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 5 — Créativité et plaisir. Tu veux créer avec méthode, perfectionner tes talents, analyser le plaisir. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Capricorn te pousse à construit dans ce domaine. Ambition structurée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : discipline à long terme. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes créations, tes loisirs, tes romances.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 5,
        'lunar_ascendant': 'Aquarius',
        'interpretation': '''**Ton mois en un mot : Analyse et originalité**

Ta Lune en Vierge en Maison 5 analyse tes créations, tes loisirs, tes romances avec minutie. L'Ascendant Aquarius innove : originalité détachée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 5 — Créativité et plaisir. Tu veux créer avec méthode, perfectionner tes talents, analyser le plaisir. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aquarius te pousse à innove dans ce domaine. Originalité détachée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Aquarius multiplie les observations sans toujours agir. Expérimentation conceptuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes créations, tes loisirs, tes romances.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 5,
        'lunar_ascendant': 'Pisces',
        'interpretation': '''**Ton mois en un mot : Ordre et chaos**

Ta Lune en Vierge en Maison 5 analyse tes créations, tes loisirs, tes romances avec minutie. L'Ascendant Pisces dissout : fluidité intuitive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 5 — Créativité et plaisir. Tu veux créer avec méthode, perfectionner tes talents, analyser le plaisir. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Pisces te pousse à dissout dans ce domaine. Fluidité intuitive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Pisces complique l'analyse Vierge. Fusion compassionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes créations, tes loisirs, tes romances.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 6,
        'lunar_ascendant': 'Aries',
        'interpretation': '''**Ton mois en un mot : Analyse et action**

Ta Lune en Vierge en Maison 6 analyse tes routines, ta santé, ton service aux autres avec minutie. L'Ascendant Aries fonce : action immédiate. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 6 — Travail quotidien et santé. Tu veux optimiser ton quotidien, perfectionner tes habitudes, servir efficacement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aries te pousse à fonce dans ce domaine. Action immédiate. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Aries crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes routines, ta santé, ton service aux autres.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 6,
        'lunar_ascendant': 'Taurus',
        'interpretation': '''**Ton mois en un mot : Perfectionnisme ancré**

Ta Lune en Vierge en Maison 6 analyse tes routines, ta santé, ton service aux autres avec minutie. L'Ascendant Taurus ancre : stabilité progressive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 6 — Travail quotidien et santé. Tu veux optimiser ton quotidien, perfectionner tes habitudes, servir efficacement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Taurus te pousse à ancre dans ce domaine. Stabilité progressive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : patience concrète. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes routines, ta santé, ton service aux autres.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 6,
        'lunar_ascendant': 'Gemini',
        'interpretation': '''**Ton mois en un mot : Analyse et curiosité**

Ta Lune en Vierge en Maison 6 analyse tes routines, ta santé, ton service aux autres avec minutie. L'Ascendant Gemini explore : curiosité multiple. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 6 — Travail quotidien et santé. Tu veux optimiser ton quotidien, perfectionner tes habitudes, servir efficacement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Gemini te pousse à explore dans ce domaine. Curiosité multiple. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Gemini multiplie les observations sans toujours agir. Dispersion intellectuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes routines, ta santé, ton service aux autres.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 6,
        'lunar_ascendant': 'Cancer',
        'interpretation': '''**Ton mois en un mot : Analyse et sensibilité**

Ta Lune en Vierge en Maison 6 analyse tes routines, ta santé, ton service aux autres avec minutie. L'Ascendant Cancer ressens : sensibilité profonde. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 6 — Travail quotidien et santé. Tu veux optimiser ton quotidien, perfectionner tes habitudes, servir efficacement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Cancer te pousse à ressens dans ce domaine. Sensibilité profonde. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Cancer complique l'analyse Vierge. Besoin de sécurité émotionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes routines, ta santé, ton service aux autres.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 6,
        'lunar_ascendant': 'Leo',
        'interpretation': '''**Ton mois en un mot : Analyse et fierté**

Ta Lune en Vierge en Maison 6 analyse tes routines, ta santé, ton service aux autres avec minutie. L'Ascendant Leo brille : fierté visible. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 6 — Travail quotidien et santé. Tu veux optimiser ton quotidien, perfectionner tes habitudes, servir efficacement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Leo te pousse à brille dans ce domaine. Fierté visible. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Leo crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes routines, ta santé, ton service aux autres.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 6,
        'lunar_ascendant': 'Virgo',
        'interpretation': '''**Ton mois en un mot : Triple analyse travail quotidien et santé**

Ta Lune en Vierge en Maison 6 analyse tes routines, ta santé, ton service aux autres avec minutie. Triple Vierge : le perfectionnisme atteint son paroxysme. Chaque détail est scruté, optimisé, amélioré sans relâche.

**Domaine activé** : Maison 6 — Travail quotidien et santé. Tu veux optimiser ton quotidien, perfectionner tes habitudes, servir efficacement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Virgo te pousse à analyse dans ce domaine. Perfectionnisme total. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : contrôle minutieux. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes routines, ta santé, ton service aux autres.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 6,
        'lunar_ascendant': 'Libra',
        'interpretation': '''**Ton mois en un mot : Analyse et recherche**

Ta Lune en Vierge en Maison 6 analyse tes routines, ta santé, ton service aux autres avec minutie. L'Ascendant Libra équilibre : recherche d'harmonie. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 6 — Travail quotidien et santé. Tu veux optimiser ton quotidien, perfectionner tes habitudes, servir efficacement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Libra te pousse à équilibre dans ce domaine. Recherche d'harmonie. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Libra multiplie les observations sans toujours agir. Indécision élégante. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes routines, ta santé, ton service aux autres.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 6,
        'lunar_ascendant': 'Scorpio',
        'interpretation': '''**Ton mois en un mot : Perfection intense**

Ta Lune en Vierge en Maison 6 analyse tes routines, ta santé, ton service aux autres avec minutie. L'Ascendant Scorpio transforme : intensité émotionnelle. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 6 — Travail quotidien et santé. Tu veux optimiser ton quotidien, perfectionner tes habitudes, servir efficacement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Scorpio te pousse à transforme dans ce domaine. Intensité émotionnelle. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Scorpio complique l'analyse Vierge. Profondeur obsessionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes routines, ta santé, ton service aux autres.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 6,
        'lunar_ascendant': 'Sagittarius',
        'interpretation': '''**Ton mois en un mot : Analyse et vision**

Ta Lune en Vierge en Maison 6 analyse tes routines, ta santé, ton service aux autres avec minutie. L'Ascendant Sagittarius explore : vision philosophique. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 6 — Travail quotidien et santé. Tu veux optimiser ton quotidien, perfectionner tes habitudes, servir efficacement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Sagittarius te pousse à explore dans ce domaine. Vision philosophique. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Sagittarius crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes routines, ta santé, ton service aux autres.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 6,
        'lunar_ascendant': 'Capricorn',
        'interpretation': '''**Ton mois en un mot : Excellence structurée**

Ta Lune en Vierge en Maison 6 analyse tes routines, ta santé, ton service aux autres avec minutie. L'Ascendant Capricorn construit : ambition structurée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 6 — Travail quotidien et santé. Tu veux optimiser ton quotidien, perfectionner tes habitudes, servir efficacement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Capricorn te pousse à construit dans ce domaine. Ambition structurée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : discipline à long terme. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes routines, ta santé, ton service aux autres.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 6,
        'lunar_ascendant': 'Aquarius',
        'interpretation': '''**Ton mois en un mot : Analyse et originalité**

Ta Lune en Vierge en Maison 6 analyse tes routines, ta santé, ton service aux autres avec minutie. L'Ascendant Aquarius innove : originalité détachée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 6 — Travail quotidien et santé. Tu veux optimiser ton quotidien, perfectionner tes habitudes, servir efficacement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aquarius te pousse à innove dans ce domaine. Originalité détachée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Aquarius multiplie les observations sans toujours agir. Expérimentation conceptuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes routines, ta santé, ton service aux autres.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 6,
        'lunar_ascendant': 'Pisces',
        'interpretation': '''**Ton mois en un mot : Ordre et chaos**

Ta Lune en Vierge en Maison 6 analyse tes routines, ta santé, ton service aux autres avec minutie. L'Ascendant Pisces dissout : fluidité intuitive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 6 — Travail quotidien et santé. Tu veux optimiser ton quotidien, perfectionner tes habitudes, servir efficacement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Pisces te pousse à dissout dans ce domaine. Fluidité intuitive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Pisces complique l'analyse Vierge. Fusion compassionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes routines, ta santé, ton service aux autres.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 7,
        'lunar_ascendant': 'Aries',
        'interpretation': '''**Ton mois en un mot : Analyse et action**

Ta Lune en Vierge en Maison 7 analyse tes couples, tes associations, tes collaborations avec minutie. L'Ascendant Aries fonce : action immédiate. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 7 — Relations et partenariats. Tu veux analyser tes relations, améliorer tes partenariats, perfectionner l'équilibre. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aries te pousse à fonce dans ce domaine. Action immédiate. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Aries crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes couples, tes associations, tes collaborations.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 7,
        'lunar_ascendant': 'Taurus',
        'interpretation': '''**Ton mois en un mot : Perfectionnisme ancré**

Ta Lune en Vierge en Maison 7 analyse tes couples, tes associations, tes collaborations avec minutie. L'Ascendant Taurus ancre : stabilité progressive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 7 — Relations et partenariats. Tu veux analyser tes relations, améliorer tes partenariats, perfectionner l'équilibre. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Taurus te pousse à ancre dans ce domaine. Stabilité progressive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : patience concrète. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes couples, tes associations, tes collaborations.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 7,
        'lunar_ascendant': 'Gemini',
        'interpretation': '''**Ton mois en un mot : Analyse et curiosité**

Ta Lune en Vierge en Maison 7 analyse tes couples, tes associations, tes collaborations avec minutie. L'Ascendant Gemini explore : curiosité multiple. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 7 — Relations et partenariats. Tu veux analyser tes relations, améliorer tes partenariats, perfectionner l'équilibre. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Gemini te pousse à explore dans ce domaine. Curiosité multiple. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Gemini multiplie les observations sans toujours agir. Dispersion intellectuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes couples, tes associations, tes collaborations.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 7,
        'lunar_ascendant': 'Cancer',
        'interpretation': '''**Ton mois en un mot : Analyse et sensibilité**

Ta Lune en Vierge en Maison 7 analyse tes couples, tes associations, tes collaborations avec minutie. L'Ascendant Cancer ressens : sensibilité profonde. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 7 — Relations et partenariats. Tu veux analyser tes relations, améliorer tes partenariats, perfectionner l'équilibre. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Cancer te pousse à ressens dans ce domaine. Sensibilité profonde. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Cancer complique l'analyse Vierge. Besoin de sécurité émotionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes couples, tes associations, tes collaborations.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 7,
        'lunar_ascendant': 'Leo',
        'interpretation': '''**Ton mois en un mot : Analyse et fierté**

Ta Lune en Vierge en Maison 7 analyse tes couples, tes associations, tes collaborations avec minutie. L'Ascendant Leo brille : fierté visible. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 7 — Relations et partenariats. Tu veux analyser tes relations, améliorer tes partenariats, perfectionner l'équilibre. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Leo te pousse à brille dans ce domaine. Fierté visible. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Leo crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes couples, tes associations, tes collaborations.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 7,
        'lunar_ascendant': 'Virgo',
        'interpretation': '''**Ton mois en un mot : Triple analyse relations et partenariats**

Ta Lune en Vierge en Maison 7 analyse tes couples, tes associations, tes collaborations avec minutie. Triple Vierge : le perfectionnisme atteint son paroxysme. Chaque détail est scruté, optimisé, amélioré sans relâche.

**Domaine activé** : Maison 7 — Relations et partenariats. Tu veux analyser tes relations, améliorer tes partenariats, perfectionner l'équilibre. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Virgo te pousse à analyse dans ce domaine. Perfectionnisme total. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : contrôle minutieux. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes couples, tes associations, tes collaborations.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 7,
        'lunar_ascendant': 'Libra',
        'interpretation': '''**Ton mois en un mot : Analyse et recherche**

Ta Lune en Vierge en Maison 7 analyse tes couples, tes associations, tes collaborations avec minutie. L'Ascendant Libra équilibre : recherche d'harmonie. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 7 — Relations et partenariats. Tu veux analyser tes relations, améliorer tes partenariats, perfectionner l'équilibre. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Libra te pousse à équilibre dans ce domaine. Recherche d'harmonie. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Libra multiplie les observations sans toujours agir. Indécision élégante. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes couples, tes associations, tes collaborations.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 7,
        'lunar_ascendant': 'Scorpio',
        'interpretation': '''**Ton mois en un mot : Perfection intense**

Ta Lune en Vierge en Maison 7 analyse tes couples, tes associations, tes collaborations avec minutie. L'Ascendant Scorpio transforme : intensité émotionnelle. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 7 — Relations et partenariats. Tu veux analyser tes relations, améliorer tes partenariats, perfectionner l'équilibre. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Scorpio te pousse à transforme dans ce domaine. Intensité émotionnelle. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Scorpio complique l'analyse Vierge. Profondeur obsessionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes couples, tes associations, tes collaborations.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 7,
        'lunar_ascendant': 'Sagittarius',
        'interpretation': '''**Ton mois en un mot : Analyse et vision**

Ta Lune en Vierge en Maison 7 analyse tes couples, tes associations, tes collaborations avec minutie. L'Ascendant Sagittarius explore : vision philosophique. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 7 — Relations et partenariats. Tu veux analyser tes relations, améliorer tes partenariats, perfectionner l'équilibre. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Sagittarius te pousse à explore dans ce domaine. Vision philosophique. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Sagittarius crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes couples, tes associations, tes collaborations.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 7,
        'lunar_ascendant': 'Capricorn',
        'interpretation': '''**Ton mois en un mot : Excellence structurée**

Ta Lune en Vierge en Maison 7 analyse tes couples, tes associations, tes collaborations avec minutie. L'Ascendant Capricorn construit : ambition structurée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 7 — Relations et partenariats. Tu veux analyser tes relations, améliorer tes partenariats, perfectionner l'équilibre. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Capricorn te pousse à construit dans ce domaine. Ambition structurée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : discipline à long terme. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes couples, tes associations, tes collaborations.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 7,
        'lunar_ascendant': 'Aquarius',
        'interpretation': '''**Ton mois en un mot : Analyse et originalité**

Ta Lune en Vierge en Maison 7 analyse tes couples, tes associations, tes collaborations avec minutie. L'Ascendant Aquarius innove : originalité détachée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 7 — Relations et partenariats. Tu veux analyser tes relations, améliorer tes partenariats, perfectionner l'équilibre. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aquarius te pousse à innove dans ce domaine. Originalité détachée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Aquarius multiplie les observations sans toujours agir. Expérimentation conceptuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes couples, tes associations, tes collaborations.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 7,
        'lunar_ascendant': 'Pisces',
        'interpretation': '''**Ton mois en un mot : Ordre et chaos**

Ta Lune en Vierge en Maison 7 analyse tes couples, tes associations, tes collaborations avec minutie. L'Ascendant Pisces dissout : fluidité intuitive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 7 — Relations et partenariats. Tu veux analyser tes relations, améliorer tes partenariats, perfectionner l'équilibre. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Pisces te pousse à dissout dans ce domaine. Fluidité intuitive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Pisces complique l'analyse Vierge. Fusion compassionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes couples, tes associations, tes collaborations.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 8,
        'lunar_ascendant': 'Aries',
        'interpretation': '''**Ton mois en un mot : Analyse et action**

Ta Lune en Vierge en Maison 8 analyse tes profondeurs, ta sexualité, les ressources partagées avec minutie. L'Ascendant Aries fonce : action immédiate. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 8 — Transformation et intimité. Tu veux transformer méthodiquement, analyser l'intimité, gérer le partagé. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aries te pousse à fonce dans ce domaine. Action immédiate. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Aries crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes profondeurs, ta sexualité, les ressources partagées.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 8,
        'lunar_ascendant': 'Taurus',
        'interpretation': '''**Ton mois en un mot : Perfectionnisme ancré**

Ta Lune en Vierge en Maison 8 analyse tes profondeurs, ta sexualité, les ressources partagées avec minutie. L'Ascendant Taurus ancre : stabilité progressive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 8 — Transformation et intimité. Tu veux transformer méthodiquement, analyser l'intimité, gérer le partagé. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Taurus te pousse à ancre dans ce domaine. Stabilité progressive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : patience concrète. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes profondeurs, ta sexualité, les ressources partagées.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 8,
        'lunar_ascendant': 'Gemini',
        'interpretation': '''**Ton mois en un mot : Analyse et curiosité**

Ta Lune en Vierge en Maison 8 analyse tes profondeurs, ta sexualité, les ressources partagées avec minutie. L'Ascendant Gemini explore : curiosité multiple. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 8 — Transformation et intimité. Tu veux transformer méthodiquement, analyser l'intimité, gérer le partagé. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Gemini te pousse à explore dans ce domaine. Curiosité multiple. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Gemini multiplie les observations sans toujours agir. Dispersion intellectuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes profondeurs, ta sexualité, les ressources partagées.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 8,
        'lunar_ascendant': 'Cancer',
        'interpretation': '''**Ton mois en un mot : Analyse et sensibilité**

Ta Lune en Vierge en Maison 8 analyse tes profondeurs, ta sexualité, les ressources partagées avec minutie. L'Ascendant Cancer ressens : sensibilité profonde. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 8 — Transformation et intimité. Tu veux transformer méthodiquement, analyser l'intimité, gérer le partagé. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Cancer te pousse à ressens dans ce domaine. Sensibilité profonde. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Cancer complique l'analyse Vierge. Besoin de sécurité émotionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes profondeurs, ta sexualité, les ressources partagées.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 8,
        'lunar_ascendant': 'Leo',
        'interpretation': '''**Ton mois en un mot : Analyse et fierté**

Ta Lune en Vierge en Maison 8 analyse tes profondeurs, ta sexualité, les ressources partagées avec minutie. L'Ascendant Leo brille : fierté visible. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 8 — Transformation et intimité. Tu veux transformer méthodiquement, analyser l'intimité, gérer le partagé. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Leo te pousse à brille dans ce domaine. Fierté visible. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Leo crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes profondeurs, ta sexualité, les ressources partagées.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 8,
        'lunar_ascendant': 'Virgo',
        'interpretation': '''**Ton mois en un mot : Triple analyse transformation et intimité**

Ta Lune en Vierge en Maison 8 analyse tes profondeurs, ta sexualité, les ressources partagées avec minutie. Triple Vierge : le perfectionnisme atteint son paroxysme. Chaque détail est scruté, optimisé, amélioré sans relâche.

**Domaine activé** : Maison 8 — Transformation et intimité. Tu veux transformer méthodiquement, analyser l'intimité, gérer le partagé. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Virgo te pousse à analyse dans ce domaine. Perfectionnisme total. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : contrôle minutieux. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes profondeurs, ta sexualité, les ressources partagées.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 8,
        'lunar_ascendant': 'Libra',
        'interpretation': '''**Ton mois en un mot : Analyse et recherche**

Ta Lune en Vierge en Maison 8 analyse tes profondeurs, ta sexualité, les ressources partagées avec minutie. L'Ascendant Libra équilibre : recherche d'harmonie. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 8 — Transformation et intimité. Tu veux transformer méthodiquement, analyser l'intimité, gérer le partagé. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Libra te pousse à équilibre dans ce domaine. Recherche d'harmonie. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Libra multiplie les observations sans toujours agir. Indécision élégante. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes profondeurs, ta sexualité, les ressources partagées.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 8,
        'lunar_ascendant': 'Scorpio',
        'interpretation': '''**Ton mois en un mot : Perfection intense**

Ta Lune en Vierge en Maison 8 analyse tes profondeurs, ta sexualité, les ressources partagées avec minutie. L'Ascendant Scorpio transforme : intensité émotionnelle. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 8 — Transformation et intimité. Tu veux transformer méthodiquement, analyser l'intimité, gérer le partagé. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Scorpio te pousse à transforme dans ce domaine. Intensité émotionnelle. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Scorpio complique l'analyse Vierge. Profondeur obsessionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes profondeurs, ta sexualité, les ressources partagées.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 8,
        'lunar_ascendant': 'Sagittarius',
        'interpretation': '''**Ton mois en un mot : Analyse et vision**

Ta Lune en Vierge en Maison 8 analyse tes profondeurs, ta sexualité, les ressources partagées avec minutie. L'Ascendant Sagittarius explore : vision philosophique. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 8 — Transformation et intimité. Tu veux transformer méthodiquement, analyser l'intimité, gérer le partagé. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Sagittarius te pousse à explore dans ce domaine. Vision philosophique. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Sagittarius crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes profondeurs, ta sexualité, les ressources partagées.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 8,
        'lunar_ascendant': 'Capricorn',
        'interpretation': '''**Ton mois en un mot : Excellence structurée**

Ta Lune en Vierge en Maison 8 analyse tes profondeurs, ta sexualité, les ressources partagées avec minutie. L'Ascendant Capricorn construit : ambition structurée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 8 — Transformation et intimité. Tu veux transformer méthodiquement, analyser l'intimité, gérer le partagé. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Capricorn te pousse à construit dans ce domaine. Ambition structurée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : discipline à long terme. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes profondeurs, ta sexualité, les ressources partagées.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 8,
        'lunar_ascendant': 'Aquarius',
        'interpretation': '''**Ton mois en un mot : Analyse et originalité**

Ta Lune en Vierge en Maison 8 analyse tes profondeurs, ta sexualité, les ressources partagées avec minutie. L'Ascendant Aquarius innove : originalité détachée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 8 — Transformation et intimité. Tu veux transformer méthodiquement, analyser l'intimité, gérer le partagé. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aquarius te pousse à innove dans ce domaine. Originalité détachée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Aquarius multiplie les observations sans toujours agir. Expérimentation conceptuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes profondeurs, ta sexualité, les ressources partagées.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 8,
        'lunar_ascendant': 'Pisces',
        'interpretation': '''**Ton mois en un mot : Ordre et chaos**

Ta Lune en Vierge en Maison 8 analyse tes profondeurs, ta sexualité, les ressources partagées avec minutie. L'Ascendant Pisces dissout : fluidité intuitive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 8 — Transformation et intimité. Tu veux transformer méthodiquement, analyser l'intimité, gérer le partagé. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Pisces te pousse à dissout dans ce domaine. Fluidité intuitive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Pisces complique l'analyse Vierge. Fusion compassionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes profondeurs, ta sexualité, les ressources partagées.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 9,
        'lunar_ascendant': 'Aries',
        'interpretation': '''**Ton mois en un mot : Analyse et action**

Ta Lune en Vierge en Maison 9 analyse tes croyances, tes voyages, ton sens de la vie avec minutie. L'Ascendant Aries fonce : action immédiate. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 9 — Philosophie et expansion. Tu veux analyser tes convictions, perfectionner ta vision, organiser l'exploration. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aries te pousse à fonce dans ce domaine. Action immédiate. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Aries crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes croyances, tes voyages, ton sens de la vie.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 9,
        'lunar_ascendant': 'Taurus',
        'interpretation': '''**Ton mois en un mot : Perfectionnisme ancré**

Ta Lune en Vierge en Maison 9 analyse tes croyances, tes voyages, ton sens de la vie avec minutie. L'Ascendant Taurus ancre : stabilité progressive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 9 — Philosophie et expansion. Tu veux analyser tes convictions, perfectionner ta vision, organiser l'exploration. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Taurus te pousse à ancre dans ce domaine. Stabilité progressive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : patience concrète. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes croyances, tes voyages, ton sens de la vie.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 9,
        'lunar_ascendant': 'Gemini',
        'interpretation': '''**Ton mois en un mot : Analyse et curiosité**

Ta Lune en Vierge en Maison 9 analyse tes croyances, tes voyages, ton sens de la vie avec minutie. L'Ascendant Gemini explore : curiosité multiple. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 9 — Philosophie et expansion. Tu veux analyser tes convictions, perfectionner ta vision, organiser l'exploration. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Gemini te pousse à explore dans ce domaine. Curiosité multiple. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Gemini multiplie les observations sans toujours agir. Dispersion intellectuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes croyances, tes voyages, ton sens de la vie.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 9,
        'lunar_ascendant': 'Cancer',
        'interpretation': '''**Ton mois en un mot : Analyse et sensibilité**

Ta Lune en Vierge en Maison 9 analyse tes croyances, tes voyages, ton sens de la vie avec minutie. L'Ascendant Cancer ressens : sensibilité profonde. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 9 — Philosophie et expansion. Tu veux analyser tes convictions, perfectionner ta vision, organiser l'exploration. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Cancer te pousse à ressens dans ce domaine. Sensibilité profonde. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Cancer complique l'analyse Vierge. Besoin de sécurité émotionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes croyances, tes voyages, ton sens de la vie.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 9,
        'lunar_ascendant': 'Leo',
        'interpretation': '''**Ton mois en un mot : Analyse et fierté**

Ta Lune en Vierge en Maison 9 analyse tes croyances, tes voyages, ton sens de la vie avec minutie. L'Ascendant Leo brille : fierté visible. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 9 — Philosophie et expansion. Tu veux analyser tes convictions, perfectionner ta vision, organiser l'exploration. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Leo te pousse à brille dans ce domaine. Fierté visible. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Leo crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes croyances, tes voyages, ton sens de la vie.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 9,
        'lunar_ascendant': 'Virgo',
        'interpretation': '''**Ton mois en un mot : Triple analyse philosophie et expansion**

Ta Lune en Vierge en Maison 9 analyse tes croyances, tes voyages, ton sens de la vie avec minutie. Triple Vierge : le perfectionnisme atteint son paroxysme. Chaque détail est scruté, optimisé, amélioré sans relâche.

**Domaine activé** : Maison 9 — Philosophie et expansion. Tu veux analyser tes convictions, perfectionner ta vision, organiser l'exploration. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Virgo te pousse à analyse dans ce domaine. Perfectionnisme total. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : contrôle minutieux. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes croyances, tes voyages, ton sens de la vie.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 9,
        'lunar_ascendant': 'Libra',
        'interpretation': '''**Ton mois en un mot : Analyse et recherche**

Ta Lune en Vierge en Maison 9 analyse tes croyances, tes voyages, ton sens de la vie avec minutie. L'Ascendant Libra équilibre : recherche d'harmonie. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 9 — Philosophie et expansion. Tu veux analyser tes convictions, perfectionner ta vision, organiser l'exploration. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Libra te pousse à équilibre dans ce domaine. Recherche d'harmonie. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Libra multiplie les observations sans toujours agir. Indécision élégante. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes croyances, tes voyages, ton sens de la vie.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 9,
        'lunar_ascendant': 'Scorpio',
        'interpretation': '''**Ton mois en un mot : Perfection intense**

Ta Lune en Vierge en Maison 9 analyse tes croyances, tes voyages, ton sens de la vie avec minutie. L'Ascendant Scorpio transforme : intensité émotionnelle. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 9 — Philosophie et expansion. Tu veux analyser tes convictions, perfectionner ta vision, organiser l'exploration. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Scorpio te pousse à transforme dans ce domaine. Intensité émotionnelle. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Scorpio complique l'analyse Vierge. Profondeur obsessionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes croyances, tes voyages, ton sens de la vie.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 9,
        'lunar_ascendant': 'Sagittarius',
        'interpretation': '''**Ton mois en un mot : Analyse et vision**

Ta Lune en Vierge en Maison 9 analyse tes croyances, tes voyages, ton sens de la vie avec minutie. L'Ascendant Sagittarius explore : vision philosophique. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 9 — Philosophie et expansion. Tu veux analyser tes convictions, perfectionner ta vision, organiser l'exploration. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Sagittarius te pousse à explore dans ce domaine. Vision philosophique. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Sagittarius crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes croyances, tes voyages, ton sens de la vie.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 9,
        'lunar_ascendant': 'Capricorn',
        'interpretation': '''**Ton mois en un mot : Excellence structurée**

Ta Lune en Vierge en Maison 9 analyse tes croyances, tes voyages, ton sens de la vie avec minutie. L'Ascendant Capricorn construit : ambition structurée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 9 — Philosophie et expansion. Tu veux analyser tes convictions, perfectionner ta vision, organiser l'exploration. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Capricorn te pousse à construit dans ce domaine. Ambition structurée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : discipline à long terme. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes croyances, tes voyages, ton sens de la vie.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 9,
        'lunar_ascendant': 'Aquarius',
        'interpretation': '''**Ton mois en un mot : Analyse et originalité**

Ta Lune en Vierge en Maison 9 analyse tes croyances, tes voyages, ton sens de la vie avec minutie. L'Ascendant Aquarius innove : originalité détachée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 9 — Philosophie et expansion. Tu veux analyser tes convictions, perfectionner ta vision, organiser l'exploration. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aquarius te pousse à innove dans ce domaine. Originalité détachée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Aquarius multiplie les observations sans toujours agir. Expérimentation conceptuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes croyances, tes voyages, ton sens de la vie.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 9,
        'lunar_ascendant': 'Pisces',
        'interpretation': '''**Ton mois en un mot : Ordre et chaos**

Ta Lune en Vierge en Maison 9 analyse tes croyances, tes voyages, ton sens de la vie avec minutie. L'Ascendant Pisces dissout : fluidité intuitive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 9 — Philosophie et expansion. Tu veux analyser tes convictions, perfectionner ta vision, organiser l'exploration. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Pisces te pousse à dissout dans ce domaine. Fluidité intuitive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Pisces complique l'analyse Vierge. Fusion compassionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes croyances, tes voyages, ton sens de la vie.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 10,
        'lunar_ascendant': 'Aries',
        'interpretation': '''**Ton mois en un mot : Analyse et action**

Ta Lune en Vierge en Maison 10 analyse ton ambition, ta réussite publique, ton impact social avec minutie. L'Ascendant Aries fonce : action immédiate. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 10 — Carrière et réputation. Tu veux exceller professionnellement, perfectionner ton image, optimiser ta carrière. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aries te pousse à fonce dans ce domaine. Action immédiate. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Aries crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton ambition, ta réussite publique, ton impact social.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 10,
        'lunar_ascendant': 'Taurus',
        'interpretation': '''**Ton mois en un mot : Perfectionnisme ancré**

Ta Lune en Vierge en Maison 10 analyse ton ambition, ta réussite publique, ton impact social avec minutie. L'Ascendant Taurus ancre : stabilité progressive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 10 — Carrière et réputation. Tu veux exceller professionnellement, perfectionner ton image, optimiser ta carrière. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Taurus te pousse à ancre dans ce domaine. Stabilité progressive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : patience concrète. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton ambition, ta réussite publique, ton impact social.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 10,
        'lunar_ascendant': 'Gemini',
        'interpretation': '''**Ton mois en un mot : Analyse et curiosité**

Ta Lune en Vierge en Maison 10 analyse ton ambition, ta réussite publique, ton impact social avec minutie. L'Ascendant Gemini explore : curiosité multiple. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 10 — Carrière et réputation. Tu veux exceller professionnellement, perfectionner ton image, optimiser ta carrière. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Gemini te pousse à explore dans ce domaine. Curiosité multiple. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Gemini multiplie les observations sans toujours agir. Dispersion intellectuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton ambition, ta réussite publique, ton impact social.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 10,
        'lunar_ascendant': 'Cancer',
        'interpretation': '''**Ton mois en un mot : Analyse et sensibilité**

Ta Lune en Vierge en Maison 10 analyse ton ambition, ta réussite publique, ton impact social avec minutie. L'Ascendant Cancer ressens : sensibilité profonde. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 10 — Carrière et réputation. Tu veux exceller professionnellement, perfectionner ton image, optimiser ta carrière. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Cancer te pousse à ressens dans ce domaine. Sensibilité profonde. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Cancer complique l'analyse Vierge. Besoin de sécurité émotionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton ambition, ta réussite publique, ton impact social.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 10,
        'lunar_ascendant': 'Leo',
        'interpretation': '''**Ton mois en un mot : Analyse et fierté**

Ta Lune en Vierge en Maison 10 analyse ton ambition, ta réussite publique, ton impact social avec minutie. L'Ascendant Leo brille : fierté visible. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 10 — Carrière et réputation. Tu veux exceller professionnellement, perfectionner ton image, optimiser ta carrière. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Leo te pousse à brille dans ce domaine. Fierté visible. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Leo crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton ambition, ta réussite publique, ton impact social.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 10,
        'lunar_ascendant': 'Virgo',
        'interpretation': '''**Ton mois en un mot : Triple analyse carrière et réputation**

Ta Lune en Vierge en Maison 10 analyse ton ambition, ta réussite publique, ton impact social avec minutie. Triple Vierge : le perfectionnisme atteint son paroxysme. Chaque détail est scruté, optimisé, amélioré sans relâche.

**Domaine activé** : Maison 10 — Carrière et réputation. Tu veux exceller professionnellement, perfectionner ton image, optimiser ta carrière. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Virgo te pousse à analyse dans ce domaine. Perfectionnisme total. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : contrôle minutieux. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton ambition, ta réussite publique, ton impact social.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 10,
        'lunar_ascendant': 'Libra',
        'interpretation': '''**Ton mois en un mot : Analyse et recherche**

Ta Lune en Vierge en Maison 10 analyse ton ambition, ta réussite publique, ton impact social avec minutie. L'Ascendant Libra équilibre : recherche d'harmonie. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 10 — Carrière et réputation. Tu veux exceller professionnellement, perfectionner ton image, optimiser ta carrière. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Libra te pousse à équilibre dans ce domaine. Recherche d'harmonie. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Libra multiplie les observations sans toujours agir. Indécision élégante. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton ambition, ta réussite publique, ton impact social.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 10,
        'lunar_ascendant': 'Scorpio',
        'interpretation': '''**Ton mois en un mot : Perfection intense**

Ta Lune en Vierge en Maison 10 analyse ton ambition, ta réussite publique, ton impact social avec minutie. L'Ascendant Scorpio transforme : intensité émotionnelle. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 10 — Carrière et réputation. Tu veux exceller professionnellement, perfectionner ton image, optimiser ta carrière. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Scorpio te pousse à transforme dans ce domaine. Intensité émotionnelle. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Scorpio complique l'analyse Vierge. Profondeur obsessionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton ambition, ta réussite publique, ton impact social.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 10,
        'lunar_ascendant': 'Sagittarius',
        'interpretation': '''**Ton mois en un mot : Analyse et vision**

Ta Lune en Vierge en Maison 10 analyse ton ambition, ta réussite publique, ton impact social avec minutie. L'Ascendant Sagittarius explore : vision philosophique. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 10 — Carrière et réputation. Tu veux exceller professionnellement, perfectionner ton image, optimiser ta carrière. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Sagittarius te pousse à explore dans ce domaine. Vision philosophique. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Sagittarius crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton ambition, ta réussite publique, ton impact social.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 10,
        'lunar_ascendant': 'Capricorn',
        'interpretation': '''**Ton mois en un mot : Excellence structurée**

Ta Lune en Vierge en Maison 10 analyse ton ambition, ta réussite publique, ton impact social avec minutie. L'Ascendant Capricorn construit : ambition structurée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 10 — Carrière et réputation. Tu veux exceller professionnellement, perfectionner ton image, optimiser ta carrière. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Capricorn te pousse à construit dans ce domaine. Ambition structurée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : discipline à long terme. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton ambition, ta réussite publique, ton impact social.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 10,
        'lunar_ascendant': 'Aquarius',
        'interpretation': '''**Ton mois en un mot : Analyse et originalité**

Ta Lune en Vierge en Maison 10 analyse ton ambition, ta réussite publique, ton impact social avec minutie. L'Ascendant Aquarius innove : originalité détachée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 10 — Carrière et réputation. Tu veux exceller professionnellement, perfectionner ton image, optimiser ta carrière. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aquarius te pousse à innove dans ce domaine. Originalité détachée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Aquarius multiplie les observations sans toujours agir. Expérimentation conceptuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton ambition, ta réussite publique, ton impact social.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 10,
        'lunar_ascendant': 'Pisces',
        'interpretation': '''**Ton mois en un mot : Ordre et chaos**

Ta Lune en Vierge en Maison 10 analyse ton ambition, ta réussite publique, ton impact social avec minutie. L'Ascendant Pisces dissout : fluidité intuitive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 10 — Carrière et réputation. Tu veux exceller professionnellement, perfectionner ton image, optimiser ta carrière. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Pisces te pousse à dissout dans ce domaine. Fluidité intuitive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Pisces complique l'analyse Vierge. Fusion compassionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton ambition, ta réussite publique, ton impact social.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 11,
        'lunar_ascendant': 'Aries',
        'interpretation': '''**Ton mois en un mot : Analyse et action**

Ta Lune en Vierge en Maison 11 analyse tes réseaux, tes idéaux, tes projets collectifs avec minutie. L'Ascendant Aries fonce : action immédiate. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 11 — Amitiés et communauté. Tu veux analyser tes amitiés, contribuer avec précision, perfectionner le collectif. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aries te pousse à fonce dans ce domaine. Action immédiate. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Aries crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes réseaux, tes idéaux, tes projets collectifs.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 11,
        'lunar_ascendant': 'Taurus',
        'interpretation': '''**Ton mois en un mot : Perfectionnisme ancré**

Ta Lune en Vierge en Maison 11 analyse tes réseaux, tes idéaux, tes projets collectifs avec minutie. L'Ascendant Taurus ancre : stabilité progressive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 11 — Amitiés et communauté. Tu veux analyser tes amitiés, contribuer avec précision, perfectionner le collectif. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Taurus te pousse à ancre dans ce domaine. Stabilité progressive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : patience concrète. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes réseaux, tes idéaux, tes projets collectifs.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 11,
        'lunar_ascendant': 'Gemini',
        'interpretation': '''**Ton mois en un mot : Analyse et curiosité**

Ta Lune en Vierge en Maison 11 analyse tes réseaux, tes idéaux, tes projets collectifs avec minutie. L'Ascendant Gemini explore : curiosité multiple. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 11 — Amitiés et communauté. Tu veux analyser tes amitiés, contribuer avec précision, perfectionner le collectif. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Gemini te pousse à explore dans ce domaine. Curiosité multiple. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Gemini multiplie les observations sans toujours agir. Dispersion intellectuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes réseaux, tes idéaux, tes projets collectifs.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 11,
        'lunar_ascendant': 'Cancer',
        'interpretation': '''**Ton mois en un mot : Analyse et sensibilité**

Ta Lune en Vierge en Maison 11 analyse tes réseaux, tes idéaux, tes projets collectifs avec minutie. L'Ascendant Cancer ressens : sensibilité profonde. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 11 — Amitiés et communauté. Tu veux analyser tes amitiés, contribuer avec précision, perfectionner le collectif. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Cancer te pousse à ressens dans ce domaine. Sensibilité profonde. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Cancer complique l'analyse Vierge. Besoin de sécurité émotionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes réseaux, tes idéaux, tes projets collectifs.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 11,
        'lunar_ascendant': 'Leo',
        'interpretation': '''**Ton mois en un mot : Analyse et fierté**

Ta Lune en Vierge en Maison 11 analyse tes réseaux, tes idéaux, tes projets collectifs avec minutie. L'Ascendant Leo brille : fierté visible. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 11 — Amitiés et communauté. Tu veux analyser tes amitiés, contribuer avec précision, perfectionner le collectif. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Leo te pousse à brille dans ce domaine. Fierté visible. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Leo crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes réseaux, tes idéaux, tes projets collectifs.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 11,
        'lunar_ascendant': 'Virgo',
        'interpretation': '''**Ton mois en un mot : Triple analyse amitiés et communauté**

Ta Lune en Vierge en Maison 11 analyse tes réseaux, tes idéaux, tes projets collectifs avec minutie. Triple Vierge : le perfectionnisme atteint son paroxysme. Chaque détail est scruté, optimisé, amélioré sans relâche.

**Domaine activé** : Maison 11 — Amitiés et communauté. Tu veux analyser tes amitiés, contribuer avec précision, perfectionner le collectif. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Virgo te pousse à analyse dans ce domaine. Perfectionnisme total. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : contrôle minutieux. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes réseaux, tes idéaux, tes projets collectifs.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 11,
        'lunar_ascendant': 'Libra',
        'interpretation': '''**Ton mois en un mot : Analyse et recherche**

Ta Lune en Vierge en Maison 11 analyse tes réseaux, tes idéaux, tes projets collectifs avec minutie. L'Ascendant Libra équilibre : recherche d'harmonie. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 11 — Amitiés et communauté. Tu veux analyser tes amitiés, contribuer avec précision, perfectionner le collectif. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Libra te pousse à équilibre dans ce domaine. Recherche d'harmonie. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Libra multiplie les observations sans toujours agir. Indécision élégante. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes réseaux, tes idéaux, tes projets collectifs.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 11,
        'lunar_ascendant': 'Scorpio',
        'interpretation': '''**Ton mois en un mot : Perfection intense**

Ta Lune en Vierge en Maison 11 analyse tes réseaux, tes idéaux, tes projets collectifs avec minutie. L'Ascendant Scorpio transforme : intensité émotionnelle. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 11 — Amitiés et communauté. Tu veux analyser tes amitiés, contribuer avec précision, perfectionner le collectif. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Scorpio te pousse à transforme dans ce domaine. Intensité émotionnelle. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Scorpio complique l'analyse Vierge. Profondeur obsessionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes réseaux, tes idéaux, tes projets collectifs.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 11,
        'lunar_ascendant': 'Sagittarius',
        'interpretation': '''**Ton mois en un mot : Analyse et vision**

Ta Lune en Vierge en Maison 11 analyse tes réseaux, tes idéaux, tes projets collectifs avec minutie. L'Ascendant Sagittarius explore : vision philosophique. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 11 — Amitiés et communauté. Tu veux analyser tes amitiés, contribuer avec précision, perfectionner le collectif. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Sagittarius te pousse à explore dans ce domaine. Vision philosophique. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Sagittarius crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes réseaux, tes idéaux, tes projets collectifs.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 11,
        'lunar_ascendant': 'Capricorn',
        'interpretation': '''**Ton mois en un mot : Excellence structurée**

Ta Lune en Vierge en Maison 11 analyse tes réseaux, tes idéaux, tes projets collectifs avec minutie. L'Ascendant Capricorn construit : ambition structurée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 11 — Amitiés et communauté. Tu veux analyser tes amitiés, contribuer avec précision, perfectionner le collectif. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Capricorn te pousse à construit dans ce domaine. Ambition structurée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : discipline à long terme. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes réseaux, tes idéaux, tes projets collectifs.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 11,
        'lunar_ascendant': 'Aquarius',
        'interpretation': '''**Ton mois en un mot : Analyse et originalité**

Ta Lune en Vierge en Maison 11 analyse tes réseaux, tes idéaux, tes projets collectifs avec minutie. L'Ascendant Aquarius innove : originalité détachée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 11 — Amitiés et communauté. Tu veux analyser tes amitiés, contribuer avec précision, perfectionner le collectif. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aquarius te pousse à innove dans ce domaine. Originalité détachée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Aquarius multiplie les observations sans toujours agir. Expérimentation conceptuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes réseaux, tes idéaux, tes projets collectifs.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 11,
        'lunar_ascendant': 'Pisces',
        'interpretation': '''**Ton mois en un mot : Ordre et chaos**

Ta Lune en Vierge en Maison 11 analyse tes réseaux, tes idéaux, tes projets collectifs avec minutie. L'Ascendant Pisces dissout : fluidité intuitive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 11 — Amitiés et communauté. Tu veux analyser tes amitiés, contribuer avec précision, perfectionner le collectif. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Pisces te pousse à dissout dans ce domaine. Fluidité intuitive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Pisces complique l'analyse Vierge. Fusion compassionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans tes réseaux, tes idéaux, tes projets collectifs.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 12,
        'lunar_ascendant': 'Aries',
        'interpretation': '''**Ton mois en un mot : Analyse et action**

Ta Lune en Vierge en Maison 12 analyse ton intériorité, tes rêves, ton lâcher-prise avec minutie. L'Ascendant Aries fonce : action immédiate. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 12 — Spiritualité et inconscient. Tu veux analyser ton inconscient, organiser le chaos intérieur, servir silencieusement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aries te pousse à fonce dans ce domaine. Action immédiate. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Aries crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton intériorité, tes rêves, ton lâcher-prise.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 12,
        'lunar_ascendant': 'Taurus',
        'interpretation': '''**Ton mois en un mot : Perfectionnisme ancré**

Ta Lune en Vierge en Maison 12 analyse ton intériorité, tes rêves, ton lâcher-prise avec minutie. L'Ascendant Taurus ancre : stabilité progressive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 12 — Spiritualité et inconscient. Tu veux analyser ton inconscient, organiser le chaos intérieur, servir silencieusement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Taurus te pousse à ancre dans ce domaine. Stabilité progressive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : patience concrète. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton intériorité, tes rêves, ton lâcher-prise.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 12,
        'lunar_ascendant': 'Gemini',
        'interpretation': '''**Ton mois en un mot : Analyse et curiosité**

Ta Lune en Vierge en Maison 12 analyse ton intériorité, tes rêves, ton lâcher-prise avec minutie. L'Ascendant Gemini explore : curiosité multiple. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 12 — Spiritualité et inconscient. Tu veux analyser ton inconscient, organiser le chaos intérieur, servir silencieusement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Gemini te pousse à explore dans ce domaine. Curiosité multiple. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Gemini multiplie les observations sans toujours agir. Dispersion intellectuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton intériorité, tes rêves, ton lâcher-prise.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 12,
        'lunar_ascendant': 'Cancer',
        'interpretation': '''**Ton mois en un mot : Analyse et sensibilité**

Ta Lune en Vierge en Maison 12 analyse ton intériorité, tes rêves, ton lâcher-prise avec minutie. L'Ascendant Cancer ressens : sensibilité profonde. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 12 — Spiritualité et inconscient. Tu veux analyser ton inconscient, organiser le chaos intérieur, servir silencieusement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Cancer te pousse à ressens dans ce domaine. Sensibilité profonde. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Cancer complique l'analyse Vierge. Besoin de sécurité émotionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton intériorité, tes rêves, ton lâcher-prise.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 12,
        'lunar_ascendant': 'Leo',
        'interpretation': '''**Ton mois en un mot : Analyse et fierté**

Ta Lune en Vierge en Maison 12 analyse ton intériorité, tes rêves, ton lâcher-prise avec minutie. L'Ascendant Leo brille : fierté visible. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 12 — Spiritualité et inconscient. Tu veux analyser ton inconscient, organiser le chaos intérieur, servir silencieusement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Leo te pousse à brille dans ce domaine. Fierté visible. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Leo crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton intériorité, tes rêves, ton lâcher-prise.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 12,
        'lunar_ascendant': 'Virgo',
        'interpretation': '''**Ton mois en un mot : Triple analyse spiritualité et inconscient**

Ta Lune en Vierge en Maison 12 analyse ton intériorité, tes rêves, ton lâcher-prise avec minutie. Triple Vierge : le perfectionnisme atteint son paroxysme. Chaque détail est scruté, optimisé, amélioré sans relâche.

**Domaine activé** : Maison 12 — Spiritualité et inconscient. Tu veux analyser ton inconscient, organiser le chaos intérieur, servir silencieusement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Virgo te pousse à analyse dans ce domaine. Perfectionnisme total. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : contrôle minutieux. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton intériorité, tes rêves, ton lâcher-prise.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 12,
        'lunar_ascendant': 'Libra',
        'interpretation': '''**Ton mois en un mot : Analyse et recherche**

Ta Lune en Vierge en Maison 12 analyse ton intériorité, tes rêves, ton lâcher-prise avec minutie. L'Ascendant Libra équilibre : recherche d'harmonie. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 12 — Spiritualité et inconscient. Tu veux analyser ton inconscient, organiser le chaos intérieur, servir silencieusement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Libra te pousse à équilibre dans ce domaine. Recherche d'harmonie. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Libra multiplie les observations sans toujours agir. Indécision élégante. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton intériorité, tes rêves, ton lâcher-prise.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 12,
        'lunar_ascendant': 'Scorpio',
        'interpretation': '''**Ton mois en un mot : Perfection intense**

Ta Lune en Vierge en Maison 12 analyse ton intériorité, tes rêves, ton lâcher-prise avec minutie. L'Ascendant Scorpio transforme : intensité émotionnelle. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 12 — Spiritualité et inconscient. Tu veux analyser ton inconscient, organiser le chaos intérieur, servir silencieusement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Scorpio te pousse à transforme dans ce domaine. Intensité émotionnelle. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Scorpio complique l'analyse Vierge. Profondeur obsessionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton intériorité, tes rêves, ton lâcher-prise.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 12,
        'lunar_ascendant': 'Sagittarius',
        'interpretation': '''**Ton mois en un mot : Analyse et vision**

Ta Lune en Vierge en Maison 12 analyse ton intériorité, tes rêves, ton lâcher-prise avec minutie. L'Ascendant Sagittarius explore : vision philosophique. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 12 — Spiritualité et inconscient. Tu veux analyser ton inconscient, organiser le chaos intérieur, servir silencieusement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Sagittarius te pousse à explore dans ce domaine. Vision philosophique. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Le feu de Sagittarius crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton intériorité, tes rêves, ton lâcher-prise.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 12,
        'lunar_ascendant': 'Capricorn',
        'interpretation': '''**Ton mois en un mot : Excellence structurée**

Ta Lune en Vierge en Maison 12 analyse ton intériorité, tes rêves, ton lâcher-prise avec minutie. L'Ascendant Capricorn construit : ambition structurée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 12 — Spiritualité et inconscient. Tu veux analyser ton inconscient, organiser le chaos intérieur, servir silencieusement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Capricorn te pousse à construit dans ce domaine. Ambition structurée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : Triple terre ou double terre : discipline à long terme. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton intériorité, tes rêves, ton lâcher-prise.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 12,
        'lunar_ascendant': 'Aquarius',
        'interpretation': '''**Ton mois en un mot : Analyse et originalité**

Ta Lune en Vierge en Maison 12 analyse ton intériorité, tes rêves, ton lâcher-prise avec minutie. L'Ascendant Aquarius innove : originalité détachée. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 12 — Spiritualité et inconscient. Tu veux analyser ton inconscient, organiser le chaos intérieur, servir silencieusement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Aquarius te pousse à innove dans ce domaine. Originalité détachée. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'air intellectuel de Aquarius multiplie les observations sans toujours agir. Expérimentation conceptuelle. L'analyse remplace parfois l'action concrète.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton intériorité, tes rêves, ton lâcher-prise.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    },
    {
        'moon_sign': 'Virgo',
        'moon_house': 12,
        'lunar_ascendant': 'Pisces',
        'interpretation': '''**Ton mois en un mot : Ordre et chaos**

Ta Lune en Vierge en Maison 12 analyse ton intériorité, tes rêves, ton lâcher-prise avec minutie. L'Ascendant Pisces dissout : fluidité intuitive. Cette combinaison crée une dynamique unique dans ta quête de perfection.

**Domaine activé** : Maison 12 — Spiritualité et inconscient. Tu veux analyser ton inconscient, organiser le chaos intérieur, servir silencieusement. Chaque imperfection te saute aux yeux et demande correction.

**Ton approche instinctive** : L'Ascendant Pisces te pousse à dissout dans ce domaine. Fluidité intuitive. La Vierge analyse et ajuste constamment.

**Tensions possibles** : L'eau émotionnelle de Pisces complique l'analyse Vierge. Fusion compassionnelle. Tu peux te perdre entre raison et ressenti.

**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer.''',
        'weekly_advice': {
            'week_1': "Identifie CE qui mérite vraiment ton attention dans ton intériorité, tes rêves, ton lâcher-prise.",
            'week_2': "Agis avec méthode sur cette priorité unique, sans te disperser.",
            'week_3': "Maintiens le cap même si ce n'est pas encore parfait. Progresse.",
            'week_4': "Évalue les progrès accomplis et célèbre le 'suffisamment bien'.",
        }
    }

]

if __name__ == "__main__":
    print(f"🚀 Insertion batch Virgo : {len(BATCH)} interprétations")
    asyncio.run(insert_batch(BATCH))
    print("✅ Batch Virgo terminé")
