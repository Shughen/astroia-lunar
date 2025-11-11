# 🚀 Installation Complète - Astroia Lunar

Guide pas-à-pas pour lancer l'app en local.

---

## 📋 Prérequis

### Obligatoire
- **Node.js** 18+ ([télécharger](https://nodejs.org))
- **Python** 3.10+ ([télécharger](https://python.org))
- **PostgreSQL** 14+ ([télécharger](https://postgresql.org))
- **Git** ([télécharger](https://git-scm.com))

### Recommandé
- **Expo Go** (app mobile iOS/Android pour tester)
- **Postman** ou **Bruno** (tester l'API)
- **VS Code** avec extensions Python + TypeScript

---

## 🛠️ Installation

### 1️⃣ Cloner le repo

```bash
git clone https://github.com/ton-username/astroia-lunar.git
cd astroia-lunar
```

### 2️⃣ Configuration environnement

```bash
# Copier .env
cp .env.example .env

# Éditer .env avec tes valeurs
nano .env  # ou ton éditeur préféré
```

**Variables critiques à configurer :**
- `DATABASE_URL` : URL PostgreSQL (ex: `postgresql://user:password@localhost:5432/astroia_lunar`)
- `EPHEMERIS_API_KEY` : Clé Ephemeris API (obtenir sur [astrology-api.io](https://astrology-api.io))
- `SECRET_KEY` : Clé secrète JWT (générer avec `openssl rand -hex 32`)

### 3️⃣ Backend (API)

```bash
# Aller dans le dossier API
cd apps/api

# Créer environnement virtuel
python -m venv venv

# Activer l'environnement
source venv/bin/activate  # macOS/Linux
# OU
venv\Scripts\activate  # Windows

# Installer dépendances
pip install -r requirements.txt

# Créer la base de données (si pas déjà fait)
createdb astroia_lunar

# Lancer les migrations
alembic upgrade head

# Démarrer l'API
python main.py
# OU avec uvicorn directement
uvicorn main:app --reload --port 8000
```

**✅ API disponible sur** `http://localhost:8000`  
**📚 Documentation** `http://localhost:8000/docs`

### 4️⃣ Frontend (Mobile)

Ouvrir un **nouveau terminal** :

```bash
# Aller dans le dossier mobile
cd apps/mobile

# Installer dépendances
npm install

# Démarrer Expo
npx expo start
```

**Options de lancement :**
- **i** : Ouvrir sur simulateur iOS
- **a** : Ouvrir sur émulateur Android
- **Scanner QR** : Ouvrir dans Expo Go (app mobile)

---

## 🧪 Tests & Validation

### Backend

```bash
cd apps/api
pytest tests/ -v
```

### Frontend

```bash
cd apps/mobile
npm test
```

### Tester l'API manuellement

1. Ouvrir `http://localhost:8000/docs`
2. Tester l'endpoint `/health` → doit retourner `{"status": "healthy"}`
3. Tester `/api/auth/register` avec :
   ```json
   {
     "email": "test@example.com",
     "password": "test123"
   }
   ```

---

## 🐛 Problèmes courants

### 1. "Module not found"
```bash
# Backend
pip install -r requirements.txt --force-reinstall

# Frontend
cd apps/mobile && npm install --force
```

### 2. "Database connection failed"
Vérifier que PostgreSQL est démarré :
```bash
# macOS (Homebrew)
brew services start postgresql@14

# Linux
sudo systemctl start postgresql

# Windows
# Démarrer via "Services" → PostgreSQL
```

### 3. "Ephemeris API error"
- Vérifier que `EPHEMERIS_API_KEY` est correcte dans `.env`
- Tester manuellement l'API sur [astrology-api.io](https://astrology-api.io)

### 4. "Expo Metro Bundler failed"
```bash
cd apps/mobile
rm -rf node_modules .expo
npm install
npx expo start --clear
```

---

## 🚢 Déploiement

### Backend (Railway)

1. Créer compte sur [Railway](https://railway.app)
2. Créer nouveau projet + PostgreSQL
3. Déployer via GitHub :
   ```bash
   railway login
   railway link [project-id]
   railway up
   ```
4. Configurer variables d'environnement dans Railway dashboard

### Frontend (Expo EAS)

```bash
cd apps/mobile
npm install -g eas-cli
eas login
eas build:configure
eas build --platform ios  # ou android
```

---

## 📖 Ressources

- [Documentation FastAPI](https://fastapi.tiangolo.com)
- [Documentation Expo](https://docs.expo.dev)
- [Ephemeris API Docs](https://astrology-api.io/docs)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org)

---

**Support :** [ton-email@astroia.app](mailto:ton-email@astroia.app)

