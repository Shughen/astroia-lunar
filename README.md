# 🌙 Astroia Lunar - Révolutions Lunaires Mensuelles

Application de bien-être centrée sur les **révolutions lunaires** mensuelles, applicable aux femmes et aux hommes.

---

## 🎯 Vision

**Astroia Lunar** propose une vision moderne et rigoureuse de l'astrologie lunaire :
- Calcul automatique de ton **thème natal** et de tes **12 révolutions lunaires annuelles**
- Interprétations mensuelles personnalisées (ascendant lunaire, maisons, aspects)
- Design mystique mais épuré (universellement accessible, non genré)
- Interface 100% française 🇫🇷

---

## 📦 Architecture (Monorepo)

```
astroia-lunar/
├── apps/
│   ├── mobile/          # Expo React Native (iOS/Android)
│   └── api/             # FastAPI + PostgreSQL
├── shared/
│   └── types/           # Types partagés (TypeScript)
├── docs/                # Documentation technique
├── .env.example         # Variables d'environnement
└── README.md
```

---

## 🚀 Quick Start

### 1️⃣ **Prérequis**
- Node.js 18+ et npm/yarn
- Python 3.10+
- PostgreSQL 14+
- Compte [Ephemeris API](https://astrology-api.io) (12€/mois)

### 2️⃣ **Installation**

```bash
# Cloner le repo
git clone https://github.com/ton-username/astroia-lunar.git
cd astroia-lunar

# Copier .env
cp .env.example .env
# Éditer .env avec tes clés (DATABASE_URL, EPHEMERIS_API_KEY)

# Backend API
cd apps/api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --reload --port 8000

# Frontend Mobile (dans un autre terminal)
cd apps/mobile
npm install
npx expo start
```

### 3️⃣ **Scripts rapides**

```bash
# Depuis la racine
npm run dev:api      # Lance FastAPI (port 8000)
npm run dev:mobile   # Lance Expo
npm run db:migrate   # Migrations Alembic
npm run db:seed      # Seed data (dev)
```

---

## 🌓 Roadmap MVP

### **Phase 1 - Core Lunaire** ✅ (4-6 semaines)
- [x] Onboarding (date/heure/lieu naissance)
- [x] Calcul thème natal via Ephemeris API
- [x] Calcul 12 révolutions lunaires annuelles
- [x] Écran "Lune du mois" (ascendant, maisons, aspects)
- [x] Liste des 12 mois avec tuiles cliquables
- [x] Interprétations textuelles (templates dynamiques)
- [x] Authentification simple (email)
- [x] Design System mystique & épuré

### **Phase 2 - Cycle Menstruel** ⏳ (2-3 semaines)
- [ ] Option d'ajout du cycle menstruel
- [ ] Croisement cycle ↔ révolution lunaire
- [ ] Insights personnalisés
- [ ] Notifications mensuelles
- [ ] Freemium : 2,99 €/mois

### **Phase 3 - Journal & ML** 🔮 (4-6 semaines)
- [ ] Journal mood/énergie/sommeil
- [ ] Corrélations via ML (scikit-learn)
- [ ] Dashboard personnel
- [ ] Export PDF rapport mensuel

---

## 🛠️ Stack Technique

### Backend
- **FastAPI** (Python 3.10+) - API REST rapide
- **PostgreSQL** + SQLAlchemy - BDD relationnelle
- **Alembic** - Migrations
- **Ephemeris API** - Calculs astrologiques (https://astrology-api.io)
- **Pydantic** - Validation des données

### Frontend
- **React Native** (Expo SDK 50+) - iOS + Android
- **TypeScript** - Typage strict
- **Expo Router** - Navigation déclarative
- **Zustand** - State management léger
- **React Native Reanimated** - Animations fluides

### Infrastructure
- **Railway** ou **Vercel** - Déploiement backend
- **PostgreSQL** (Railway/Supabase) - BDD managée
- **Expo EAS** - Build & déploiement mobile

---

## 📚 Endpoints API Principaux

### Auth
- `POST /api/auth/register` - Inscription
- `POST /api/auth/login` - Connexion

### Astrologie
- `POST /api/natal-chart` - Calcule le thème natal
  ```json
  {
    "date": "1990-05-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
  }
  ```

- `GET /api/lunar-returns` - Récupère les 12 révolutions lunaires
- `GET /api/lunar-returns/:month` - Détails d'un mois (YYYY-MM)
  ```json
  {
    "month": "2025-11",
    "lunar_ascendant": "Taureau",
    "moon_house": 4,
    "aspects": [...],
    "interpretation": "Ce mois, ta Lune revient en Maison 4..."
  }
  ```

### Cycle (Phase 2)
- `POST /api/cycle/start` - Début cycle menstruel
- `GET /api/cycle/predictions` - Prédictions cycle ↔ lune

---

## 🎨 Design System

Couleurs principales (inspirées de ton `astroia-app`) :
- **Violet foncé** : `#1a0b2e`, `#2d1b4e`
- **Accent mystique** : `#b794f6` (violet clair)
- **Or lunaire** : `#ffd700`
- **Texte** : `#ffffff` (titres), `#a0a0b0` (secondaire)

Typographie :
- **Titres** : Montserrat Bold
- **Corps** : Inter Regular

---

## 🧪 Tests

```bash
# Backend
cd apps/api
pytest tests/ -v

# Frontend
cd apps/mobile
npm test
```

---

## 📖 Documentation Complète

- [Architecture détaillée](docs/ARCHITECTURE.md)
- [Calculs astrologiques](docs/ASTRO_CALCULATIONS.md)
- [API Reference](docs/API.md)
- [UI/UX Guidelines](docs/DESIGN.md)

---

## 💰 Coûts Mensuels (Estimé)

- **Ephemeris API** : 12 €/mois (plan Standard, 10k req/mois)
- **Railway/Vercel** : 5-10 €/mois (Hobby/Pro)
- **PostgreSQL** : Inclus (Railway) ou 10 €/mois (Supabase)
- **Total** : ~20-30 €/mois

---

## 🤝 Contribution

Projet en phase MVP, contributions bienvenues après Phase 1 validée.

---

## 📄 Licence

Propriétaire - © 2025 Astroia. Tous droits réservés.

---

## 📧 Contact

Pour toute question : [ton-email@astroia.app](mailto:ton-email@astroia.app)

---

**Fait avec 🌙 et ☕ par l'équipe Astroia**

