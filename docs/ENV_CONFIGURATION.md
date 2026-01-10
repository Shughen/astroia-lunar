# 🔧 Configuration des Variables d'Environnement

Ce document décrit toutes les variables d'environnement nécessaires pour Astroia Lunar API.

## 📋 Fichier .env à créer

Créez un fichier `.env` à la racine du projet avec les variables suivantes :

```env
# ===========================================
# DATABASE
# ===========================================
DATABASE_URL=postgresql://user:password@localhost:5432/astroia_lunar
DATABASE_POOL_SIZE=10
DATABASE_MAX_OVERFLOW=20

# ===========================================
# RAPIDAPI - Best Astrology API
# ===========================================
# Obtenez votre clé sur: https://rapidapi.com/
RAPIDAPI_KEY=votre_cle_rapidapi_ici
RAPIDAPI_HOST=best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com
BASE_RAPID_URL=https://best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com
NATAL_URL=https://best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com/api/v3/charts/natal

# ===========================================
# LUNA PACK ENDPOINTS (P1)
# ===========================================
# Ces chemins sont des defaults. Ne les changez que si l'API provider évolue.
LUNAR_RETURN_REPORT_PATH=/api/v3/charts/lunar_return/report
VOID_OF_COURSE_PATH=/api/v3/moon/void_of_course
LUNAR_MANSIONS_PATH=/api/v3/moon/mansions

# ===========================================
# TRANSITS ENDPOINTS (P2)
# ===========================================
NATAL_TRANSITS_PATH=/api/v3/transits/natal
LUNAR_RETURN_TRANSITS_PATH=/api/v3/transits/lunar_return

# ===========================================
# CALENDAR ENDPOINTS (P3)
# ===========================================
LUNAR_PHASES_PATH=/api/v3/moon/phases
LUNAR_EVENTS_PATH=/api/v3/moon/events
LUNAR_CALENDAR_YEAR_PATH=/api/v3/moon/calendar/year

# ===========================================
# API CONFIGURATION
# ===========================================
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=True
APP_ENV=development

# ===========================================
# JWT SECURITY
# ===========================================
# Générez une clé forte avec: openssl rand -hex 32
SECRET_KEY=votre_secret_key_securise_ici
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# ===========================================
# FRONTEND
# ===========================================
FRONTEND_URL=http://localhost:8081

# ===========================================
# TIMEZONE
# ===========================================
TZ=Europe/Paris

# ===========================================
# LEGACY (à migrer)
# ===========================================
EPHEMERIS_API_KEY=
EPHEMERIS_API_URL=https://api.astrology-api.io/v1
```

## 🔐 Variables Critiques

### RAPIDAPI_KEY (obligatoire)
- **Obtention** : Inscrivez-vous sur [RapidAPI](https://rapidapi.com/) et souscrivez à "Best Astrology API"
- **Format** : Chaîne alphanumér ique de ~50 caractères
- **Sécurité** : Ne JAMAIS commiter cette clé dans le code

### SECRET_KEY (obligatoire)
- **Génération** : `openssl rand -hex 32`
- **Usage** : Signature des tokens JWT
- **Sécurité** : Unique par environnement, ne jamais partager

### DATABASE_URL (obligatoire)
- **Format** : `postgresql://user:password@host:port/database`
- **Exemple local** : `postgresql://postgres:postgres@localhost:5432/astroia_lunar`
- **Production** : Utiliser des variables d'environnement sécurisées

## 🛠️ Configuration des Endpoints Provider

Les chemins d'endpoints RapidAPI sont configurables via ENV pour s'adapter aux évolutions de l'API :

| Variable | Default | Description |
|----------|---------|-------------|
| `LUNAR_RETURN_REPORT_PATH` | `/api/v3/charts/lunar_return/report` | Rapport mensuel révolution lunaire |
| `VOID_OF_COURSE_PATH` | `/api/v3/moon/void_of_course` | Fenêtres VoC |
| `LUNAR_MANSIONS_PATH` | `/api/v3/moon/mansions` | Mansions lunaires (28) |
| `NATAL_TRANSITS_PATH` | `/api/v3/transits/natal` | Transits sur thème natal |
| `LUNAR_RETURN_TRANSITS_PATH` | `/api/v3/transits/lunar_return` | Transits sur révolution lunaire |
| `LUNAR_PHASES_PATH` | `/api/v3/moon/phases` | Phases lunaires précises |
| `LUNAR_EVENTS_PATH` | `/api/v3/moon/events` | Événements lunaires spéciaux |
| `LUNAR_CALENDAR_YEAR_PATH` | `/api/v3/moon/calendar/year` | Calendrier lunaire annuel |

⚠️ **Note** : Ces endpoints sont basés sur la documentation supposée du provider. Si certains n'existent pas, ils retourneront une erreur 502 avec un message clair.

## 🚀 Quick Start

```bash
# 1. Copier ce template dans .env
cp docs/ENV_CONFIGURATION.md .env
# (Puis éditer .env avec vos vraies valeurs)

# 2. Générer une SECRET_KEY
openssl rand -hex 32

# 3. Créer la base de données
createdb astroia_lunar

# 4. Lancer l'API
cd apps/api
source .venv/bin/activate
uvicorn main:app --reload
```

## 🔍 Vérification

Une fois l'API lancée, testez la configuration :

```bash
curl http://localhost:8000/health
```

Réponse attendue :
```json
{
  "status": "healthy",
  "checks": {
    "database": "connected",
    "rapidapi_config": "configured"
  }
}
```

## 🐛 Troubleshooting

### "missing_key" dans /health
➡️ Vérifiez que `RAPIDAPI_KEY` est bien définie dans `.env`

### "database error: connection refused"
➡️ PostgreSQL n'est pas démarré : `pg_ctl start` ou `brew services start postgresql`

### "502 Bad Gateway" sur endpoints lunaires
➡️ Vérifiez que votre clé RapidAPI est valide et que vous avez des crédits disponibles

---

**Fait avec 🌙 par l'équipe Astroia**

