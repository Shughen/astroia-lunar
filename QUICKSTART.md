# ⚡ QUICKSTART - Astroia Lunar (2 minutes)

Lancement ultra-rapide pour développement local.

---

## 🏃‍♂️ TL;DR

```bash
# 1. Cloner + configurer
git clone https://github.com/ton-username/astroia-lunar.git
cd astroia-lunar
cp .env.example .env
nano .env  # Éditer DATABASE_URL + EPHEMERIS_API_KEY

# 2. Backend (Terminal 1)
cd apps/api
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
createdb astroia_lunar  # Si pas déjà fait
alembic upgrade head
python main.py

# 3. Frontend (Terminal 2)
cd apps/mobile
npm install
npx expo start
```

**✅ API** : `http://localhost:8000/docs`  
**✅ Mobile** : Scanner QR avec Expo Go

---

## 📦 Ce qui a été créé

### Backend (`apps/api/`)
- ✅ FastAPI + PostgreSQL + SQLAlchemy
- ✅ 3 endpoints principaux :
  - `POST /api/auth/register` - Inscription
  - `POST /api/natal-chart` - Calcul thème natal
  - `POST /api/lunar-returns/generate` - Génère 12 révolutions lunaires
- ✅ Client Ephemeris API
- ✅ Interprétations textuelles automatiques
- ✅ JWT Auth

### Frontend (`apps/mobile/`)
- ✅ Expo React Native + TypeScript
- ✅ 3 écrans :
  - **Onboarding** : Inscription + données naissance
  - **Home** : Grille des 12 mois lunaires
  - **Détail mois** : Interprétation + stats
- ✅ Zustand state management
- ✅ Design System mystique (violet/or)

---

## 🧪 Tester rapidement

### 1. Créer un utilisateur

```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@lunar.app",
    "password": "test123"
  }'
```

### 2. Calculer thème natal

```bash
curl -X POST http://localhost:8000/api/natal-chart \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [TON_TOKEN]" \
  -d '{
    "date": "1990-05-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris"
  }'
```

### 3. Générer révolutions lunaires

```bash
curl -X POST http://localhost:8000/api/lunar-returns/generate \
  -H "Authorization: Bearer [TON_TOKEN]"
```

---

## 🌙 Flow utilisateur complet

1. **Inscription** (`/onboarding`)
   - Email + Password
   - Date/heure/lieu de naissance + coordonnées
   
2. **Calcul automatique**
   - Thème natal calculé via Ephemeris API
   - 12 révolutions lunaires générées pour l'année
   
3. **Accueil** (`/index`)
   - Grille des 12 mois avec ascendant lunaire
   
4. **Détail mois** (`/lunar-month/[month]`)
   - Ascendant, Maison, Signe de la Lune
   - Interprétation textuelle personnalisée
   - Aspects majeurs

---

## 🎨 Aperçu Design

```
┌──────────────────────────┐
│   🌙 Astroia Lunar      │  Gradient violet foncé
│                          │
│  ┌──────┐  ┌──────┐    │
│  │ JAN  │  │ FEV  │    │  Tuiles mois
│  │Taureau│  │Gémeaux│   │
│  └──────┘  └──────┘    │
│                          │
│  ... (10 autres)         │
└──────────────────────────┘
```

---

## 🔧 Variables .env essentielles

```bash
# Base de données
DATABASE_URL=postgresql://user:password@localhost:5432/astroia_lunar

# Ephemeris API (obtenir sur astrology-api.io)
EPHEMERIS_API_KEY=your_api_key_here

# JWT Secret (générer avec: openssl rand -hex 32)
SECRET_KEY=change-me-in-production

# Frontend
EXPO_PUBLIC_API_URL=http://localhost:8000
```

---

## 📝 Prochaines étapes (Phase 2-3)

### Phase 2 - Cycle Menstruel
- [ ] Ajout optionnel du cycle
- [ ] Croisement cycle ↔ révolution lunaire
- [ ] Insights personnalisés
- [ ] Notifications mensuelles
- [ ] Freemium : 2,99 €/mois

### Phase 3 - Journal & ML
- [ ] Journal mood/énergie/sommeil
- [ ] Corrélations ML (scikit-learn)
- [ ] Dashboard personnel
- [ ] Export PDF rapport mensuel

---

## 💡 Tips développement

### Hot reload
- Backend : Uvicorn `--reload` activé
- Frontend : Expo Fast Refresh automatique

### Debug API
- Docs interactives : `http://localhost:8000/docs`
- Logs : Visibles dans le terminal backend

### Reset DB (dev)
```bash
dropdb astroia_lunar
createdb astroia_lunar
alembic upgrade head
```

---

## 🐞 Bug ? Suggestion ?

- **Issues** : [GitHub Issues](https://github.com/ton-username/astroia-lunar/issues)
- **Email** : [ton-email@astroia.app](mailto:ton-email@astroia.app)

---

**Bon dev ! 🚀✨**

