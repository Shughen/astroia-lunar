# API Lunar Interpretation V2

**Version** : 2.0.0
**Date** : 2026-01-23
**Base URL** : `https://api.astroia.app` (production) | `http://localhost:8000` (dev)

## 📚 Table des matières

1. [Introduction](#introduction)
2. [Authentification](#authentification)
3. [Endpoints](#endpoints)
4. [Modèles de données](#modèles-de-données)
5. [Codes d'erreur](#codes-derreur)
6. [Exemples d'utilisation](#exemples-dutilisation)
7. [Migration V1 → V2](#migration-v1--v2)

---

## 🎯 Introduction

L'API Lunar Interpretation V2 fournit des interprétations astrologiques lunaires personnalisées, générées dynamiquement via IA (Claude Opus 4.5) avec fallback intelligent vers templates.

### Nouveautés V2

- ✨ **Génération à la volée** : Interprétations générées dynamiquement (pas de pré-génération)
- 🔄 **Fallback hiérarchique** : 4 niveaux (DB temporelle → Claude → DB templates → Hardcoded)
- 📊 **Metadata enrichies** : source, model_used, version, generated_at
- 🔁 **Force regenerate** : Endpoint dédié pour régénérer à la demande
- 📈 **Stats utilisateur** : Endpoint metadata avec stats d'utilisation

### Architecture V2

```
Layer 1: FAITS ASTRONOMIQUES (LunarReturn) - Immuables
Layer 2: NARRATION IA (LunarInterpretation) - Temporelle, régénérable
Layer 3: CACHE APPLICATION (LunarReport) - Court terme (1h)
Layer 4: FALLBACK TEMPLATES - Statiques (1728 templates)
```

---

## 🔐 Authentification

Toutes les routes V2 nécessitent un **JWT token** valide.

### Obtenir un token

```bash
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response** :
```json
{
  "access_token": "<JWT_TOKEN_HERE>",
  "token_type": "bearer"
}
```

### Utiliser le token

```bash
# Header Authorization requis
Authorization: Bearer <JWT_TOKEN_HERE>
```

---

## 📡 Endpoints

### 1. GET /api/lunar-returns/current/report

Récupère le rapport lunaire du mois en cours avec interprétation V2.

**Auth** : ✅ Requis (JWT)

**Query Parameters** :
- Aucun (utilise le thème natal de l'utilisateur authentifié)

**Response** :
```json
{
  "lunar_return": {
    "month": "2026-01",
    "return_date": "2026-01-15T14:23:45Z",
    "moon_sign": "Aries",
    "moon_house": 4,
    "lunar_ascendant": "Leo",
    "aspects": [
      {
        "first_planet": "Moon",
        "second_planet": "Sun",
        "aspect": "Trine",
        "orb": 2.5
      }
    ]
  },
  "interpretation": {
    "full": "Interprétation complète du mois...",
    "climate": "Ambiance émotionnelle...",
    "focus": "Zones de focus...",
    "approach": "Approche du mois...",
    "weekly_advice": {
      "week_1": "Conseil semaine 1...",
      "week_2": "Conseil semaine 2...",
      "week_3": "Conseil semaine 3...",
      "week_4": "Conseil semaine 4..."
    }
  },
  "metadata": {
    "source": "claude",
    "model_used": "claude-opus-4-5-20251101",
    "version": 2,
    "generated_at": "2026-01-23T10:30:00Z"
  }
}
```

**Champs metadata** :
- `source` : `"db_temporal"` (cache), `"claude"` (génération), `"db_template"` (fallback 1), `"hardcoded"` (fallback 2)
- `model_used` : Nom du modèle Claude ou `"template"` ou `"placeholder"`
- `version` : Version du prompt (2 = V2)
- `generated_at` : Timestamp de génération

**Exemples d'utilisation** :
```bash
# cURL
curl -X GET "http://localhost:8000/api/lunar-returns/current/report" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"

# JavaScript (fetch)
const response = await fetch('http://localhost:8000/api/lunar-returns/current/report', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});
const data = await response.json();
console.log(data.metadata.source); // "claude" ou "db_temporal"
```

**Erreurs** :
- `401 Unauthorized` : Token manquant ou invalide
- `404 Not Found` : Utilisateur n'a pas de thème natal
- `503 Service Unavailable` : Tous les fallbacks ont échoué

---

### 2. POST /api/lunar/interpretation/regenerate

Force la régénération d'une interprétation (bypass cache).

**Auth** : ✅ Requis (JWT)

**Body** :
```json
{
  "lunar_return_id": 123,
  "subject": "full"
}
```

**Parameters** :
- `lunar_return_id` (integer, required) : ID de la révolution lunaire
- `subject` (string, optional) : Type d'interprétation (`"full"`, `"climate"`, `"focus"`, `"approach"`). Défaut : `"full"`

**Response** :
```json
{
  "interpretation": "Nouvelle interprétation régénérée...",
  "weekly_advice": {
    "week_1": "Nouveau conseil...",
    "week_2": "...",
    "week_3": "...",
    "week_4": "..."
  },
  "metadata": {
    "source": "claude",
    "model_used": "claude-opus-4-5-20251101",
    "subject": "full",
    "regenerated_at": "2026-01-23T11:45:00Z",
    "forced": true
  }
}
```

**Use Cases** :
1. Amélioration du prompt (nouvelle version du modèle)
2. Qualité insatisfaisante (utilisateur veut une nouvelle génération)
3. Debug/test génération Claude temps réel

**Exemples d'utilisation** :
```bash
# cURL
curl -X POST "http://localhost:8000/api/lunar/interpretation/regenerate" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"lunar_return_id": 123, "subject": "full"}'

# JavaScript (fetch)
const response = await fetch('http://localhost:8000/api/lunar/interpretation/regenerate', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    lunar_return_id: 123,
    subject: 'full'
  })
});
```

**Erreurs** :
- `401 Unauthorized` : Token manquant ou invalide
- `403 Forbidden` : Utilisateur ne possède pas ce LunarReturn
- `404 Not Found` : LunarReturn introuvable
- `422 Validation Error` : lunar_return_id manquant

---

### 3. GET /api/lunar/interpretation/metadata

Récupère les statistiques d'utilisation des interprétations pour l'utilisateur authentifié.

**Auth** : ✅ Requis (JWT)

**Query Parameters** :
- Aucun (utilise l'utilisateur authentifié)

**Response** :
```json
{
  "total_interpretations": 42,
  "models_used": [
    {
      "model": "claude-opus-4-5-20251101",
      "count": 30,
      "percentage": 71.4
    },
    {
      "model": "template",
      "count": 12,
      "percentage": 28.6
    }
  ],
  "cached_rate": 85.7,
  "last_generated": "2026-01-23T10:30:00Z",
  "cached": false
}
```

**Champs** :
- `total_interpretations` : Nombre total d'interprétations générées
- `models_used` : Répartition par modèle (Claude, template, etc.)
- `cached_rate` : Taux d'utilisation du cache (%)
- `last_generated` : Date de la dernière génération
- `cached` : `true` si réponse depuis cache applicatif (TTL 10min)

**Exemples d'utilisation** :
```bash
# cURL
curl -X GET "http://localhost:8000/api/lunar/interpretation/metadata" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"

# JavaScript (fetch)
const response = await fetch('http://localhost:8000/api/lunar/interpretation/metadata', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});
const data = await response.json();
console.log(`Cache rate: ${data.cached_rate}%`);
```

**Erreurs** :
- `401 Unauthorized` : Token manquant ou invalide

---

## 📊 Modèles de données

### LunarInterpretation (DB)

Table : `lunar_interpretations`

```sql
CREATE TABLE lunar_interpretations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    lunar_return_id INTEGER NOT NULL REFERENCES lunar_returns(id) ON DELETE CASCADE,
    subject VARCHAR(50) NOT NULL,  -- 'full' | 'climate' | 'focus' | 'approach'
    version INTEGER NOT NULL DEFAULT 2,
    lang VARCHAR(10) NOT NULL DEFAULT 'fr',
    input_json JSONB NOT NULL,  -- Contexte complet envoyé à Claude
    output_text TEXT NOT NULL,  -- Interprétation générée
    weekly_advice JSONB,        -- Conseils hebdomadaires
    model_used VARCHAR(50),     -- 'claude-opus-4-5', 'template', etc.
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE (lunar_return_id, subject, lang, version)  -- Idempotence
);
```

**Indexes** :
- `idx_lunar_interpretations_user` : `user_id`
- `idx_lunar_interpretations_return` : `lunar_return_id`
- `idx_lunar_interpretations_unique` : `(lunar_return_id, subject, lang, version)` UNIQUE

### LunarInterpretationTemplate (Fallback)

Table : `lunar_interpretation_templates`

1728 templates statiques utilisés comme fallback.

---

## ⚠️ Codes d'erreur

| Code | Message | Description |
|------|---------|-------------|
| 401 | Unauthorized | JWT token manquant ou invalide |
| 403 | Forbidden | Accès refusé (ownership check) |
| 404 | Not Found | Ressource introuvable (LunarReturn, NatalChart) |
| 422 | Validation Error | Paramètres invalides |
| 503 | Service Unavailable | Tous les fallbacks ont échoué |

---

## 💡 Exemples d'utilisation

### Exemple 1 : Récupérer rapport lunaire

```typescript
// React Native (apps/mobile)
import { getLunarReport } from '@/services/api';

const LunarReportScreen = () => {
  const [report, setReport] = useState(null);

  useEffect(() => {
    const fetchReport = async () => {
      try {
        const data = await getLunarReport();
        setReport(data);
        console.log('Source:', data.metadata.source); // "claude" ou "db_temporal"
      } catch (error) {
        console.error('Error:', error);
      }
    };
    fetchReport();
  }, []);

  return (
    <View>
      <Text>{report?.interpretation.full}</Text>
      <Text style={{ fontSize: 10, color: 'gray' }}>
        Source: {report?.metadata.source} ({report?.metadata.model_used})
      </Text>
    </View>
  );
};
```

### Exemple 2 : Force regenerate

```typescript
// Bouton "Régénérer l'interprétation"
const handleRegenerate = async (lunarReturnId: number) => {
  try {
    const response = await fetch('/api/lunar/interpretation/regenerate', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        lunar_return_id: lunarReturnId,
        subject: 'full'
      })
    });

    if (response.ok) {
      const data = await response.json();
      alert('Interprétation régénérée !');
      // Mettre à jour l'UI avec data.interpretation
    }
  } catch (error) {
    alert('Erreur lors de la régénération');
  }
};
```

### Exemple 3 : Afficher stats metadata

```typescript
// Dashboard utilisateur
const MetadataStats = () => {
  const [metadata, setMetadata] = useState(null);

  useEffect(() => {
    const fetchMetadata = async () => {
      const response = await fetch('/api/lunar/interpretation/metadata', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await response.json();
      setMetadata(data);
    };
    fetchMetadata();
  }, []);

  return (
    <View>
      <Text>Total interprétations : {metadata?.total_interpretations}</Text>
      <Text>Cache rate : {metadata?.cached_rate}%</Text>
      <Text>Modèles utilisés :</Text>
      {metadata?.models_used.map(m => (
        <Text key={m.model}>- {m.model}: {m.percentage}%</Text>
      ))}
    </View>
  );
};
```

---

## 🔄 Migration V1 → V2

### Changements majeurs

| Aspect | V1 | V2 |
|--------|----|----|
| Stockage | Fichiers JSON statiques | DB temporelle + templates |
| Génération | Pré-générée (1728 combinaisons) | À la volée (Claude Opus 4.5) |
| Fallback | Fichiers JSON → hardcoded | DB temporelle → Claude → DB templates → hardcoded |
| Metadata | Aucune | source, model_used, version, generated_at |
| Régénération | Impossible | Endpoint dédié `/regenerate` |
| Stats | Aucune | Endpoint `/metadata` avec stats |

### Guide de migration frontend

**Avant (V1)** :
```typescript
// Interprétation statique, toujours la même
const interpretation = lunarReport.interpretation;
```

**Après (V2)** :
```typescript
// Interprétation dynamique avec metadata
const interpretation = lunarReport.interpretation.full;
const source = lunarReport.metadata.source; // "claude" ou "db_temporal"

// Afficher la source à l'utilisateur (optionnel)
if (source === 'claude') {
  console.log('✨ Interprétation générée par IA');
} else if (source === 'db_temporal') {
  console.log('⚡ Interprétation depuis cache');
}
```

### Rétrocompatibilité

✅ Les routes V1 continuent de fonctionner via legacy wrapper :
- `GET /api/lunar-returns/current/report` retourne format compatible V1+V2
- Champ `interpretation` contient à la fois V1 (texte simple) et V2 (objet avec metadata)

---

## 📚 Ressources

- **Architecture V2** : `docs/LUNAR_ARCHITECTURE_V2.md`
- **Plan migration** : `docs/MIGRATION_PLAN.md`
- **Monitoring** : `docs/MONITORING.md`
- **Code source** :
  - Generator : `services/lunar_interpretation_generator.py`
  - Routes : `routes/lunar_returns.py`, `routes/lunar.py`
  - Modèles : `models/lunar_interpretation.py`
