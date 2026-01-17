# 🌙 Astroia Lunar

> Application astrologique universelle centrée sur les révolutions lunaires et les thèmes natals

**Astroia Lunar** est un spin-off de l'application **Astro.IA**, conçu pour analyser les rythmes émotionnels et énergétiques mensuels via les révolutions lunaires, en intégrant hommes et femmes dans une approche scientifique et intuitive de l'astrologie.

---

## 🎯 Vision du Projet

L'objectif est de créer une application qui combine :

- 🌟 **Données d'éphémérides précises** via API externe (RapidAPI - Best Astrology API)
- 📊 **Personnalisation via data science** et machine learning
- 🎨 **Interface mobile élégante** avec design mystique moderne
- 🔮 **Révolutions lunaires** pour analyser les cycles mensuels
- 📖 **Thèmes natals complets** avec positions planétaires et aspects

---

## 🏗️ Architecture

### Monorepo Structure

```
astroia-lunar/
├── apps/
│   ├── api/                # Backend FastAPI (Python)
│   │   ├── routes/         # Routes API (auth, natal, lunar_returns)
│   │   ├── models/         # Modèles SQLAlchemy
│   │   ├── services/       # Services métier (ephemeris, rapidapi)
│   │   ├── alembic/        # Migrations de base de données
│   │   ├── config.py       # Configuration centralisée
│   │   ├── database.py     # Connexion PostgreSQL
│   │   └── main.py         # Point d'entrée FastAPI
│   │
│   └── mobile/             # Frontend Expo React Native
│       ├── app/            # Écrans (Expo Router)
│       ├── components/     # Composants réutilisables
│       ├── services/       # Client API
│       ├── stores/         # State management (Zustand)
│       └── constants/      # Thème et constantes
│
├── .env                    # Variables d'environnement
├── README.md              # Ce fichier
└── QUICKSTART.md          # Guide de démarrage rapide
```

---

## 🛠️ Stack Technique

| Domaine | Technologie | Description |
|---------|-------------|-------------|
| **Backend** | FastAPI + PostgreSQL | API REST avec auth JWT |
| **Frontend** | Expo / React Native | App mobile cross-platform |
| **State** | Zustand | Gestion d'état légère |
| **ORM** | SQLAlchemy + Alembic | Migrations et modèles |
| **Auth** | JWT (python-jose) | Tokens sécurisés |
| **API Astro** | RapidAPI - Best Astrology API | Calculs éphémérides précis |
| **Base** | PostgreSQL 16 | Base de données relationnelle |
| **Doc API** | Swagger UI | Documentation interactive |
| **Design** | Violet/Or/Noir | Thème mystique moderne |

---

## ✅ Fonctionnalités Implémentées

### 🔐 Authentification
- ✅ Inscription utilisateur avec données de naissance
- ✅ Connexion via JWT
- ✅ Protection des routes par token
- ✅ Profil utilisateur

### 🌟 Thème Natal
- ✅ Calcul complet via RapidAPI
- ✅ Positions planétaires (Soleil, Lune, Mercure, Vénus, Mars, Jupiter, Saturne, Uranus, Neptune, Pluton)
- ✅ Points spéciaux (Ascendant, MC, Chiron, Nœuds, Lilith)
- ✅ 12 maisons astrologiques (système Placidus)
- ✅ Calcul des aspects (conjonctions, trigones, carrés, sextiles, oppositions, etc.)
- ✅ Phase lunaire
- ✅ Sauvegarde en base de données

### 🌙 Révolutions Lunaires
- ✅ Génération automatique de 12 mois
- ✅ Calcul de l'ascendant lunaire
- ✅ Position de la Lune dans les maisons
- ✅ Interprétations textuelles
- ✅ Stockage PostgreSQL

### 📱 Interface Mobile
- ✅ Écran d'onboarding
- ✅ Grille des 12 mois lunaires
- ✅ Détail par mois avec interprétation
- ✅ Design mystique (violet/or)
- ✅ Navigation fluide (Expo Router)

### 🌙 Luna Pack (P1) - Fonctionnalités Avancées
> Trio de fonctionnalités différenciantes basées sur les cycles lunaires

- ✅ **Lunar Return Report** : Rapport mensuel complet de révolution lunaire avec analyse détaillée
- ✅ **Void of Course (VoC)** : Détection des fenêtres VoC avec alertes en temps réel
- ✅ **Lunar Mansions (28)** : Système des 28 mansions lunaires avec interprétations quotidiennes

#### Endpoints API Luna Pack
```http
POST /api/lunar/return/report     # Génération du rapport mensuel
POST /api/lunar/voc                # Statut Void of Course
POST /api/lunar/mansion            # Mansion lunaire du moment
GET  /api/lunar/voc/current        # VoC actuel depuis cache
GET  /api/lunar/mansion/today      # Mansion du jour depuis cache
GET  /api/lunar/return/report/history/{user_id}  # Historique utilisateur
```

#### Tables de stockage Luna Pack
- **lunar_reports** : Rapports mensuels par utilisateur (user_id, month, report JSONB)
- **lunar_voc_windows** : Fenêtres Void of Course (start_at, end_at, source JSONB)
- **lunar_mansions_daily** : Mansion quotidienne (date, mansion_id, data JSONB)

#### Écrans mobiles Luna Pack
- 📱 **app/lunar/index.tsx** : Interface de test des 3 fonctionnalités
- 📱 **app/lunar/report.tsx** : Affichage détaillé du rapport lunaire

---

## 🚀 Installation et Configuration

### Prérequis

- Python 3.10+
- Node.js 18+
- PostgreSQL 16+
- Expo Go (sur mobile)

### 1. Configuration initiale

Clonez le repository et créez le fichier `.env` à la racine :

```bash
cd astroia-lunar
```

Créez `.env` :

```env
# Database
DATABASE_URL=postgresql://<votre_user>@localhost:5432/astroia_lunar

# RapidAPI - Best Astrology API
RAPIDAPI_KEY=<votre_cle_rapidapi>
RAPIDAPI_HOST=best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com
NATAL_URL=https://best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com/api/v3/charts/natal

# Security
SECRET_KEY=<generer_avec_openssl_rand_hex_32>

# API Config
API_HOST=0.0.0.0
API_PORT=8000
APP_ENV=development
```

### 2. Backend (FastAPI)

```bash
cd apps/api

# Créer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sur Windows

# Installer les dépendances
pip install -r requirements.txt

# Créer la base de données
createdb astroia_lunar

# Appliquer les migrations
alembic upgrade head

# Note: Pour le Luna Pack, la migration 2e3f9a1c4b5d_luna_pack_tables ajoute 3 tables

# Lancer l'API
uvicorn main:app --reload --port 8000
```

L'API est accessible sur **http://localhost:8000**
Documentation Swagger : **http://localhost:8000/docs**

### 3. Mobile (Expo)

```bash
cd apps/mobile

# Créer .env local
echo "EXPO_PUBLIC_API_URL=http://localhost:8000" > .env

# Installer les dépendances
npm install --legacy-peer-deps

# Lancer Expo
npx expo start
```

Scannez le QR code avec **Expo Go** sur votre téléphone.

---

## 📡 Endpoints API

### Authentication
- `POST /api/auth/register` - Inscription
- `POST /api/auth/login` - Connexion
- `GET /api/auth/me` - Profil utilisateur

### Thème Natal
- `POST /api/natal-chart` - Calculer et sauvegarder le thème natal
- `GET /api/natal-chart` - Récupérer le thème natal
- `POST /api/natal-chart/external` - Calcul via RapidAPI (pass-through)

### Révolutions Lunaires
- `POST /api/lunar-returns/generate` - Générer 12 révolutions lunaires
- `GET /api/lunar-returns` - Liste des révolutions
- `GET /api/lunar-returns/{month}` - Détail par mois

### Luna Pack (P1)
- `POST /api/lunar/return/report` - Générer un rapport lunaire mensuel
- `POST /api/lunar/voc` - Obtenir le statut Void of Course
- `POST /api/lunar/mansion` - Obtenir la mansion lunaire
- `GET /api/lunar/voc/current` - Vérifier le VoC actuel (cache)
- `GET /api/lunar/mansion/today` - Récupérer la mansion du jour (cache)
- `GET /api/lunar/return/report/history/{user_id}` - Historique des rapports

### Système
- `GET /` - Status
- `GET /health` - Health check

---

## 🔮 Intégration RapidAPI

Le projet utilise **Best Astrology API** via RapidAPI pour des calculs éphémérides précis.

### Configuration

Ajoutez dans votre `.env` à la racine de `apps/api/` :

```env
RAPIDAPI_KEY=<votre_cle_rapidapi>
RAPIDAPI_HOST=best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com
BASE_RAPID_URL=https://best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com
```

### Format du payload

```json
{
  "subject": {
    "name": "Nom de la personne",
    "birth_data": {
      "year": 1989,
      "month": 4,
      "day": 15,
      "hour": 17,
      "minute": 55,
      "timezone": "Europe/Paris",
      "latitude": 48.8566,
      "longitude": 2.3522
    }
  }
}
```

### Données retournées

- Positions de toutes les planètes (signe, degré, maison)
- Ascendant, Descendant, MC, IC
- 12 maisons astrologiques
- Aspects planétaires (conjonction, trigone, carré, sextile, opposition, etc.)
- Phase lunaire
- Points spéciaux (Chiron, Nœuds Nord/Sud, Lilith)

---

## 🗄️ Modèles de Données

### User
```python
- id: Integer (PK)
- email: String (unique)
- hashed_password: String
- birth_date, birth_time, birth_place: String
- birth_latitude, birth_longitude: String
- birth_timezone: String
- is_active, is_premium: Boolean
- created_at, updated_at: DateTime
```

### NatalChart
```python
- id: Integer (PK)
- user_id: Integer (FK)
- sun_sign, moon_sign, ascendant: String
- planets: JSON (positions planétaires)
- houses: JSON (cuspides des maisons)
- aspects: JSON (aspects planétaires)
- raw_data: JSON (données brutes RapidAPI)
```

### LunarReturn
```python
- id: Integer (PK)
- user_id: Integer (FK)
- month: String (YYYY-MM)
- lunar_ascendant: String
- moon_house: Integer
- interpretation: Text
- themes: Array[String]
- raw_data: JSON
```

### Luna Pack Tables

#### LunarReport
```python
- id: Integer (PK)
- user_id: Integer (FK → users.id, CASCADE)
- month: String (YYYY-MM, indexed)
- report: JSONB (réponse brute provider)
- created_at: DateTime (timestamptz)
# Index composite: (user_id, month)
```

#### LunarVocWindow
```python
- id: Integer (PK)
- start_at: DateTime (timestamptz, indexed)
- end_at: DateTime (timestamptz, indexed)
- source: JSONB (données brutes)
- created_at: DateTime (timestamptz)
# Index composite: (start_at, end_at)
```

#### LunarMansionDaily
```python
- id: Integer (PK)
- date: Date (unique, indexed)
- mansion_id: Integer (1-28)
- data: JSONB (données complètes)
- created_at: DateTime (timestamptz)
```

---

## 🎨 Design System

### Couleurs

```typescript
colors = {
  darkBg: ['#1a0b2e', '#2d1b4e'],      // Dégradé de fond
  cardBg: '#2a1a4e',                    // Cartes
  accent: '#b794f6',                    // Violet lunaire
  gold: '#ffd700',                      // Or mystique
  text: '#ffffff',                      // Texte principal
  textMuted: '#a0a0b0',                 // Texte secondaire
}
```

### Typographie

- **Headings** : Bold, grandes tailles
- **Body** : Regular, lisible
- **Emojis** : Utilisés pour les signes astrologiques

---

## 🧪 Tests

### Tester l'API avec cURL

```bash
# Health check
curl http://localhost:8000/health

# Inscription
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "motdepasse123",
    "birth_date": "1989-04-15",
    "birth_time": "17:55",
    "birth_latitude": "48.8566",
    "birth_longitude": "2.3522",
    "birth_place_name": "Paris",
    "birth_timezone": "Europe/Paris"
  }'

# Thème natal via RapidAPI
curl -X POST http://localhost:8000/api/natal-chart/external \
  -H "Content-Type: application/json" \
  -d '{
    "subject": {
      "name": "Test",
      "birth_data": {
        "year": 1989,
        "month": 4,
        "day": 15,
        "hour": 17,
        "minute": 55,
        "timezone": "Europe/Paris",
        "latitude": 48.8566,
        "longitude": 2.3522
      }
    }
  }'
```

---

## 🔜 Roadmap

### Phase 2 - Intelligence & Data Science
- [ ] Croisement thème natal ↔ révolutions lunaires
- [ ] Génération automatique d'insights personnalisés
- [ ] Table d'apprentissage (statistiques)
- [ ] Graphiques et dashboard

### Phase 3 - Journal & Machine Learning
- [ ] Journal émotionnel et énergétique
- [ ] Modèles de corrélation (scikit-learn)
- [ ] Prédictions des pics lunaires personnels
- [ ] Rapport PDF mensuel

### Phase 4 - Features Avancées
- [ ] Synastrie (compatibilité entre 2 personnes)
- [ ] Transits planétaires en temps réel
- [ ] Progressions secondaires
- [ ] Révolution solaire annuelle
- [ ] Notifications pour événements astrologiques importants

---

## 📚 Documentation Technique

### Services

#### `services/ephemeris_rapidapi.py`
Client HTTP asynchrone pour l'API RapidAPI.

```python
async def create_natal_chart(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Calcule un thème natal via RapidAPI"""
```

#### `services/ephemeris.py`
Service legacy pour d'autres API d'éphémérides (à migrer).

### Routes

- `routes/auth.py` - Authentification JWT
- `routes/natal.py` - Thèmes natals
- `routes/lunar_returns.py` - Révolutions lunaires

### Migrations

```bash
# Créer une nouvelle migration
alembic revision --autogenerate -m "Description"

# Appliquer les migrations
alembic upgrade head

# Revenir en arrière
alembic downgrade -1
```

---

## 🤝 Contribution

Ce projet est actuellement en développement privé. Pour toute question :
- Email : remi@astroia.com
- GitHub : [@remibeaurain](https://github.com/remibeaurain)

---

## 📄 Licence

© 2025 Astroia - Tous droits réservés

---

## 🔧 Troubleshooting

### Problèmes Courants Backend (API)

#### 1. Erreur "ModuleNotFoundError" lors du démarrage

**Symptôme:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
cd apps/api
pip install -r requirements.txt
```

#### 2. Erreur de connexion à la base de données

**Symptôme:** `sqlalchemy.exc.OperationalError: could not connect to server`

**Solutions:**
- Vérifier que PostgreSQL est démarré : `brew services list`
- Vérifier les variables d'environnement dans `.env` :
  - `DATABASE_URL` doit pointer vers votre base de données locale
  - Format : `postgresql://username:password@localhost:5432/astroia_lunar`
- Créer la base de données si elle n'existe pas :
  ```bash
  psql -U postgres -c "CREATE DATABASE astroia_lunar;"
  ```

#### 3. Erreur 401 avec l'API Anthropic

**Symptôme:** `anthropic.AuthenticationError: Error code: 401`

**Solution:**
- Vérifier que `ANTHROPIC_API_KEY` est défini dans `.env`
- Vérifier que la clé est valide et active sur https://console.anthropic.com
- Ne jamais commiter `.env` ou afficher la clé API

#### 4. Tests échouent avec "connection refused"

**Symptôme:** Tests pytest échouent avec erreur de connexion

**Solution:**
```bash
cd apps/api
# Utiliser SQLite pour les tests
pytest -q
# SQLite est configuré automatiquement pour les tests
```

### Problèmes Courants Mobile (Expo)

#### 1. Erreur "Cannot find module '@react-native-async-storage/async-storage'"

**Solution:**
```bash
cd apps/mobile
npm install
npx expo install @react-native-async-storage/async-storage
```

#### 2. App ne se connecte pas à l'API backend

**Symptômes:**
- Erreurs réseau dans l'app
- `AxiosError: Network Error`

**Solutions:**
- Vérifier que l'API backend est démarrée : `http://localhost:8000/health`
- Sur simulateur iOS : utiliser `http://localhost:8000`
- Sur appareil physique : utiliser l'IP locale (ex: `http://192.168.1.100:8000`)
- Modifier `API_BASE_URL` dans `apps/mobile/services/api.ts` si nécessaire

#### 3. Build échoue avec erreur TypeScript

**Symptôme:** `TS2304: Cannot find name 'X'`

**Solutions:**
```bash
cd apps/mobile
npm run typecheck  # Vérifier les erreurs TypeScript
npm run lint       # Vérifier les erreurs de syntaxe
```

#### 4. Expo Go ne trouve pas l'app

**Solutions:**
- Vérifier que vous êtes sur le même réseau WiFi
- Redémarrer le serveur Expo : `npm start -- --clear`
- Scanner à nouveau le QR code

### Problèmes Courants Tests E2E (Maestro)

#### 1. "Unable to launch app"

**Symptôme:** Tests Maestro échouent avec "Unable to launch app com.remi.astroia"

**Solutions:**
- Démarrer un simulateur iOS ou émulateur Android
- Builder et installer l'app : `npm run ios` ou `npm run android`
- Vérifier que l'app est installée sur le simulateur

#### 2. "Unable to locate a Java Runtime"

**Symptôme:** Maestro ne trouve pas Java

**Solutions:**
```bash
# Installer Java 17
brew install openjdk@17

# Configurer JAVA_HOME
echo 'export JAVA_HOME=/opt/homebrew/opt/openjdk@17' >> ~/.zshrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Vérifier
java -version
```

### Obtenir de l'Aide

- 📚 Consulter la documentation dans `docs/`
- 🔍 Chercher dans les issues GitHub
- 💬 Contacter l'équipe de développement

---

## 🙏 Remerciements

- **RapidAPI - Best Astrology API** pour les calculs éphémérides
- **FastAPI** pour le framework backend
- **Expo** pour le framework mobile
- **PostgreSQL** pour la base de données

---

## 📝 Notes de Version

### v1.0.0 (Novembre 2025)
- ✅ Architecture monorepo complète
- ✅ Backend FastAPI avec auth JWT
- ✅ Intégration RapidAPI fonctionnelle
- ✅ Calcul de thèmes natals complets
- ✅ Génération de 12 révolutions lunaires
- ✅ App mobile Expo opérationnelle
- ✅ Design mystique moderne
- ✅ Base de données PostgreSQL avec migrations

---

**Fait avec 🌙 et ⭐ par l'équipe Astroia**
