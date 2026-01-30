# Maestro E2E Tests - Astroia Lunar Mobile

## Introduction

Ce dossier contient les tests end-to-end (E2E) pour l'application mobile Astroia Lunar, utilisant [Maestro](https://maestro.mobile.dev/).

Maestro permet de tester l'application mobile de manière automatisée sur iOS et Android.

## Prérequis

### 1. Installer Maestro

```bash
curl -Ls https://get.maestro.mobile.dev | bash
```

### 2. Installer Java Runtime (requis par Maestro)

Maestro nécessite Java 8 ou supérieur. Plusieurs options:

**Option A: Via Homebrew (recommandé)**
```bash
# Fixer les permissions Homebrew si nécessaire
sudo chown -R $(whoami) /opt/homebrew /Users/$(whoami)/Library/Caches/Homebrew

# Installer OpenJDK 17
brew install openjdk@17

# Configurer JAVA_HOME
echo 'export JAVA_HOME=/opt/homebrew/opt/openjdk@17' >> ~/.zshrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Option B: Via Oracle Java**
Télécharger depuis [java.com](https://www.java.com/)

**Option C: Via Temurin (AdoptOpenJDK)**
```bash
brew install --cask temurin
```

### 3. Vérifier l'installation

```bash
# Vérifier Java
java --version

# Vérifier Maestro
maestro -v
```

## Structure des tests

```
maestro/
├── flows/              # Tests E2E organisés par flow
│   ├── 1_home_load.yaml               # Test: chargement écran Home
│   ├── 2_onboarding_to_home.yaml      # Test: onboarding complet → Home
│   ├── 3_home_to_lunar_report.yaml    # Test: Home → Rapport lunaire
│   ├── 4_home_to_voc.yaml             # Test: Home → VoC actuel
│   ├── 5_home_to_transits.yaml        # Test: Home → Transits majeurs
│   └── 6_journal_create_entry.yaml    # Test: Home → Journal → Créer entrée
├── config.yaml         # Configuration globale (optionnel)
└── README.md           # Cette documentation
```

## Lancer les tests

### Lancer tous les tests

```bash
cd apps/mobile
maestro test maestro/flows/
```

### Lancer un test spécifique

```bash
cd apps/mobile
maestro test maestro/flows/1_home_load.yaml
```

### Lancer via npm script

```bash
cd apps/mobile
npm run e2e
```

## Tests disponibles

### 1. Home Load (`1_home_load.yaml`)

Vérifie le chargement correct de l'écran d'accueil:
- Lance l'application
- Vérifie la présence de "Révolution Lunaire"
- Vérifie la présence de "Void of Course"
- Prend un screenshot

### 2. Onboarding to Home (`2_onboarding_to_home.yaml`)

Vérifie le parcours complet d'onboarding jusqu'au Home:
- Lance l'application (premier lancement)
- Welcome screen → continuer
- Profile setup → remplir prénom et date
- Consent RGPD → accepter
- Disclaimer médical → accepter
- Slides onboarding → terminer
- Calcul thème natal → attendre résultat
- Vérifier arrivée sur Home avec widgets visibles

### 3. Home to Lunar Report (`3_home_to_lunar_report.yaml`)

Vérifie la navigation vers le rapport lunaire:
- Lance l'application
- Tap sur "Current Lunar Card"
- Navigue vers rapport lunaire
- Vérifie header (mois, dates, moon sign, ascendant)
- Vérifie section "Climat général"
- Vérifie section "Axes dominants"
- Vérifie section "Aspects majeurs"
- Retour au Home

### 4. Home to VoC (`4_home_to_voc.yaml`)

Vérifie la navigation vers le détail VoC:
- Lance l'application
- Tap sur "VoC Widget"
- Navigue vers détail VoC
- Vérifie statut VoC (actif/inactif)
- Vérifie prochaine fenêtre visible
- Retour au Home

### 5. Home to Transits (`5_home_to_transits.yaml`)

Vérifie la navigation vers l'overview des transits:
- Lance l'application
- Tap sur "Transits Widget"
- Navigue vers overview transits
- Vérifie liste transits visible
- Vérifie 3 transits majeurs affichés (filtrage major_only actif)
- Retour au Home

### 6. Journal Create Entry (`6_journal_create_entry.yaml`)

Vérifie la création d'une entrée journal:
- Lance l'application
- Tap sur "Journal Prompt"
- Navigue vers journal
- Créer entrée (texte)
- Sauvegarder
- Vérifie entrée visible dans liste
- Vérifie badge "✅ Aujourd'hui" affiché
- Retour au Home avec badge journal actif

## Commandes utiles

```bash
# Lancer Maestro Studio (mode interactif)
maestro studio

# Lancer avec un appareil spécifique
maestro test --device "iPhone 15" maestro/flows/1_home_load.yaml

# Afficher les appareils disponibles
maestro test --help

# Débugger un test
maestro test --debug maestro/flows/1_home_load.yaml
```

## Configuration iOS/Android

Par défaut, les tests utilisent `appId: com.remi.astroia` défini dans chaque flow.

Pour tester sur des environnements différents, vous pouvez créer un fichier `config.yaml`:

```yaml
# maestro/config.yaml
appId: com.remi.astroia  # App ID par défaut

# Configuration iOS
ios:
  appId: com.remi.astroia

# Configuration Android
android:
  appId: com.remi.astroia
```

## Écrire de nouveaux tests

Les tests Maestro utilisent le format YAML. Voici un exemple basique:

```yaml
appId: com.remi.astroia
---
- launchApp
- assertVisible: "Mon texte"
- tapOn: "Bouton"
- inputText: "Saisie utilisateur"
- takeScreenshot: mon_screenshot
```

Documentation complète: https://maestro.mobile.dev/

## Troubleshooting

### Maestro ne trouve pas Java

```bash
# Vérifier JAVA_HOME
echo $JAVA_HOME

# Si vide, configurer manuellement
export JAVA_HOME=/opt/homebrew/opt/openjdk@17
export PATH="$JAVA_HOME/bin:$PATH"
```

### L'app ne se lance pas

```bash
# Vérifier que l'app est installée
maestro test --debug maestro/flows/1_home_load.yaml

# Relancer l'app manuellement puis relancer le test
```

### Tests échouent de manière aléatoire

Ajouter des délais dans le flow:

```yaml
- launchApp
- runFlow:
    wait: 2000  # Attendre 2 secondes
- assertVisible: "Mon élément"
```

## Roadmap

- [x] Test onboarding complet
- [x] Test révolution lunaire flow
- [x] Test Void of Course details
- [x] Test création d'entrée journal
- [x] Test transits majeurs overview
- [x] **Capture complète des screenshots (22+ écrans) pour publication**
- [ ] Test timeline lunaire (12 mois)
- [ ] Test notifications (si simulateur le permet)
- [ ] Tests de régression complets

## Capture des Screenshots

Un flow dédié permet de capturer automatiquement tous les écrans de l'application pour publication sur Google Play Store.

### Flow de Capture

**Fichier** : `maestro/flows/capture-all-screens.yaml`

Capture automatiquement :
- 1 écran authentification
- 7 écrans onboarding
- 3 écrans tabs (Home, Calendar, Profile)
- 11 écrans secondaires (rapports, VoC, transits, journal, natal chart, settings)
- 2 écrans modals (bottom sheet)
- 2 écrans debug (optionnels)

**Total** : 22-26 screenshots selon configuration

### Utilisation

```bash
# Workflow complet (recommandé)
npm run screenshots:full

# Capture uniquement
npm run screenshots:capture

# Organisation uniquement
npm run screenshots:organize

# Validation IA uniquement
npm run screenshots:validate
```

### Documentation Complète

Voir `docs/SCREENSHOTS_WORKFLOW.md` pour :
- Prérequis détaillés
- Installation
- Guide d'utilisation complet
- Architecture des scripts
- Validation avec Claude Opus 4.5
- Troubleshooting
- FAQ

## Ressources

- [Documentation Maestro](https://maestro.mobile.dev/)
- [Exemples de flows](https://maestro.mobile.dev/examples)
- [API Reference](https://maestro.mobile.dev/api-reference)
