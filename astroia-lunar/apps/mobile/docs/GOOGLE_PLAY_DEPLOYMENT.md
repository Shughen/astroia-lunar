# Guide Distribution Google Play - Lunation

**Date** : 2026-01-28
**Application** : Lunation (Astrologie Lunaire)
**Package** : com.shughen85.astroialunar
**Status** : Pret pour Internal Testing

---

## Table des Matieres

1. [Prerequisites](#prerequisites)
2. [Preparation des Assets](#preparation-des-assets)
3. [Configuration EAS](#configuration-eas)
4. [Build Android](#build-android)
5. [Google Play Console](#google-play-console)
6. [Internal Testing](#internal-testing)
7. [Checklist Pre-Soumission](#checklist-pre-soumission)

---

## Prerequisites

### Comptes Requis

| Compte | URL | Cout |
|--------|-----|------|
| Google Play Developer | https://play.google.com/console/signup | $25 (one-time) |
| Expo (EAS) | https://expo.dev | Gratuit |

### Outils

```bash
# Verifier EAS CLI installe
npx eas --version
# Si pas installe: npm install -g eas-cli

# Se connecter a EAS
npx eas login
npx eas whoami
```

### Backend Deploye

L'API doit etre deployee AVANT de builder l'app mobile :
- [ ] Backend deploye sur Render (voir `apps/api/docs/DEPLOYMENT_RENDER.md`)
- [ ] URL de production obtenue : `https://lunation-api.onrender.com`
- [ ] Health check OK : `curl https://[URL]/health`

---

## Preparation des Assets

### Icones (OBLIGATOIRE - A CREER)

Les icones actuelles sont des **placeholders Expo** et seront rejetees par Google Play.

| Fichier | Dimensions | Usage |
|---------|-----------|-------|
| `assets/icon.png` | 1024x1024 | Icone principale app |
| `assets/adaptive-icon.png` | 1024x1024 | Android Adaptive Icon (foreground) |
| `assets/splash-icon.png` | 1024x1024 | Splash screen |
| `assets/favicon.png` | 48x48 | Web (optionnel) |

#### Specifications Android Adaptive Icon

Pour Android 8.0+, l'icone adaptative est composee de :
- **Foreground** : `adaptive-icon.png` (votre logo/icone)
- **Background** : Couleur definie dans `app.json`

```json
// app.json - configuration actuelle
"android": {
  "adaptiveIcon": {
    "foregroundImage": "./assets/adaptive-icon.png",
    "backgroundColor": "#ffffff"
  }
}
```

#### Outils Recommandes pour Creer les Icones

1. **Figma** (gratuit) - https://figma.com
2. **Canva** (gratuit) - https://canva.com
3. **EasyAppIcon** - https://easyappicon.com (genere toutes les tailles)
4. **AppIcon.co** - https://appicon.co

#### Conseils Design

- Icone simple et reconnaissable (lune, croissant, etc.)
- Eviter le texte (illisible en petit)
- Couleurs contrastees
- Format PNG avec transparence pour adaptive-icon
- Zone de securite : garder 66% du contenu au centre

### Screenshots (OBLIGATOIRE pour Google Play)

Minimum **2 screenshots**, recommande **4-8**.

| Type | Dimensions | Quantite |
|------|------------|----------|
| Phone | 1080x1920 ou 1080x2400 | Min 2, max 8 |
| 7" Tablet | 1200x1920 | Optionnel |
| 10" Tablet | 1600x2560 | Optionnel |

#### Ecrans Recommandes pour Screenshots

1. **Home** - Vue principale avec position lunaire
2. **Lunar Report** - Interpretation du cycle lunaire
3. **Transits** - Vue des transits planetaires
4. **Theme Natal** - Chart astrologique (si implemente)

#### Outils pour Screenshots

- **Figma** avec mockups device
- **Shotsnapp** - https://shotsnapp.com
- **Previewed** - https://previewed.app

### Feature Graphic (OBLIGATOIRE)

Banniere promotionnelle pour Google Play :
- **Dimensions** : 1024x500 px
- **Format** : PNG ou JPG
- **Contenu** : Logo + tagline + visuels app

---

## Configuration EAS

### 1. Verifier eas.json

```bash
# apps/mobile/eas.json
{
  "cli": {
    "version": ">= 16.28.0",
    "appVersionSource": "remote"
  },
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "preview": {
      "distribution": "internal"
    },
    "production": {
      "autoIncrement": true
    }
  },
  "submit": {
    "production": {}
  }
}
```

### 2. Configurer .env Production

Creer ou modifier `apps/mobile/.env` :

```bash
# === PRODUCTION CONFIG ===
EXPO_PUBLIC_API_URL=https://lunation-api.onrender.com
EXPO_PUBLIC_DEV_AUTH_BYPASS=false

# OAuth (optionnel - peut etre configure plus tard)
# EXPO_PUBLIC_GOOGLE_CLIENT_ID_ANDROID=xxx.apps.googleusercontent.com
```

### 3. Verifier app.json

```bash
# apps/mobile/app.json - config actuelle
{
  "expo": {
    "name": "Lunation",
    "slug": "astroia-lunar",
    "version": "1.0.0",
    "android": {
      "package": "com.shughen85.astroialunar",
      "versionCode": 1
    }
  }
}
```

---

## Build Android

### 1. Build Production AAB

```bash
cd apps/mobile

# Build Android App Bundle (AAB) pour Google Play
npx eas build --platform android --profile production
```

### 2. Suivre le Build

- EAS affiche un lien vers le build en cours
- Duree : ~10-15 minutes
- Resultat : fichier `.aab`

### 3. Telecharger le AAB

Apres le build :
```bash
# Option 1 : Via le lien fourni par EAS
# Option 2 : Via Expo dashboard > Builds > Download

# Le fichier sera nomme quelque chose comme :
# astroia-lunar-[version].aab
```

---

## Google Play Console

### 1. Creer un Compte Developer

1. Aller sur https://play.google.com/console/signup
2. Accepter les conditions
3. Payer $25 (paiement unique)
4. Verification d'identite (peut prendre 24-48h)

### 2. Creer l'Application

1. **Create app**
2. Remplir les informations :

| Champ | Valeur |
|-------|--------|
| App name | Lunation |
| Default language | French (France) |
| App or game | App |
| Free or paid | Free |

3. Accepter les declarations

### 3. Configurer le Store Listing

#### Main Store Listing

| Champ | Contenu |
|-------|---------|
| **App name** | Lunation |
| **Short description** (80 chars max) | Astrologie lunaire personnalisee - Suivez vos cycles lunaires |
| **Full description** | Voir ci-dessous |

**Full Description (exemple)** :
```
Lunation est votre guide d'astrologie lunaire personnalise.

FONCTIONNALITES :
- Revolutions lunaires personnalisees basees sur votre thème natal
- Interpretations IA de qualite professionnelle
- Suivi des transits planetaires
- Position actuelle de la Lune
- Journal lunaire pour noter vos observations

COMMENT CA MARCHE :
1. Entrez vos donnees de naissance
2. Recevez votre interpretation lunaire mensuelle
3. Suivez les energies du cycle en cours

Lunation utilise l'intelligence artificielle pour generer des interpretations astrologiques uniques et personnalisees.

Application gratuite. Respecte votre vie privee.
```

#### Graphics

| Asset | Requis |
|-------|--------|
| App icon (512x512) | Oui |
| Feature graphic (1024x500) | Oui |
| Phone screenshots (min 2) | Oui |
| 7-inch tablet screenshots | Non |
| 10-inch tablet screenshots | Non |

### 4. App Content

Remplir les questionnaires obligatoires :

#### Privacy Policy (OBLIGATOIRE)

Creer une page web ou Google Doc avec votre politique de confidentialite.

**Contenu minimum** :
- Donnees collectees (email, donnees naissance)
- Utilisation des donnees
- Stockage et securite
- Droits utilisateurs (RGPD)

**Exemple URL** : `https://lunation.app/privacy` ou Google Doc public

#### Data Safety

Declarer les donnees collectees :
- [x] Personal info > Email address
- [x] Personal info > Date of birth
- [x] Location > Approximate location (lieu de naissance)

#### Content Rating

Remplir le questionnaire IARC :
- Pas de violence
- Pas de contenu sexuel
- Pas de jeux d'argent
- Resultat probable : **PEGI 3** / **Everyone**

#### Target Audience

- [x] 18+ (astrologie = public adulte recommande)

---

## Internal Testing

### 1. Creer une Release Internal Testing

1. **Release** > **Testing** > **Internal testing**
2. **Create new release**
3. Upload le fichier `.aab`
4. Ajouter les release notes :
```
Version 1.0.0 - Initial release
- Interpretations lunaires personnalisees
- Suivi des transits
- Position lunaire en temps reel
```

### 2. Configurer les Testeurs

1. **Testers** > **Create email list**
2. Nom : "Internal Testers"
3. Ajouter les emails des testeurs (max 100)

### 3. Publier en Internal Testing

1. **Review release**
2. **Start rollout to Internal testing**

### 4. Distribuer aux Testeurs

Apres publication (~1-3 jours pour premiere soumission) :
1. Les testeurs recoivent un lien d'invitation
2. Lien format : `https://play.google.com/apps/internaltest/[ID]`
3. Testeurs doivent accepter l'invitation sur leur device Android

---

## Checklist Pre-Soumission

### Assets

- [ ] `icon.png` remplace (pas le placeholder Expo)
- [ ] `adaptive-icon.png` remplace
- [ ] `splash-icon.png` remplace
- [ ] App icon 512x512 pour Google Play
- [ ] Feature graphic 1024x500
- [ ] Minimum 2 phone screenshots

### Configuration

- [ ] `EXPO_PUBLIC_API_URL` pointe vers Render production
- [ ] `EXPO_PUBLIC_DEV_AUTH_BYPASS=false`
- [ ] Backend deploye et health check OK
- [ ] Version et versionCode corrects dans app.json

### Google Play Console

- [ ] Compte developer cree ($25)
- [ ] App creee dans Console
- [ ] Privacy policy URL fournie
- [ ] Data safety rempli
- [ ] Content rating complete
- [ ] Store listing complete

### Build

- [ ] Build EAS production reussi
- [ ] AAB telecharge
- [ ] Test sur device Android avant upload

---

## Timeline Estimee

| Etape | Duree |
|-------|-------|
| Creer icones et assets | 1-2h |
| Configurer .env production | 15min |
| Build EAS | 15min |
| Configurer Google Play Console | 1-2h |
| Review Google (premiere soumission) | 1-3 jours |
| **Total** | 2-4h + attente review |

---

## Troubleshooting

### Build EAS echoue

```bash
# Verifier les logs
npx eas build:list

# Rebuild avec logs verbeux
npx eas build --platform android --profile production --clear-cache
```

### AAB rejete par Google Play

Causes courantes :
- Version/versionCode deja existant (incrementer)
- Signature differente (utiliser meme keystore)
- Package name incorrect

### Testeurs ne recoivent pas l'invitation

- Verifier email correct
- Testeurs doivent avoir compte Google
- Delai possible 24-48h premiere fois

---

## Ressources

- [Expo EAS Build](https://docs.expo.dev/build/introduction/)
- [Google Play Console Help](https://support.google.com/googleplay/android-developer)
- [Android Adaptive Icons](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive)
- [Store Listing Guidelines](https://support.google.com/googleplay/android-developer/answer/9859152)

---

**Derniere mise a jour** : 2026-01-28
