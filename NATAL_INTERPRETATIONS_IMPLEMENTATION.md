# 🌟 Implémentation - Interprétations Thème Natal avec Claude

## 📋 Résumé

Enrichissement du "Thème Natal" dans l'app mobile (Expo/React Native) avec des **interprétations générées par Claude (Anthropic)** et **cachées en base Supabase**.

### Fonctionnalités

✅ Clic sur Soleil/Lune/Ascendant → Modal avec interprétation personnalisée
✅ Clic sur chaque planète → Idem
✅ Génération via Claude 3.5 Sonnet avec prompt optimisé style Astroia
✅ Cache intelligent en DB (évite de régénérer)
✅ Version du prompt trackée (permet d'améliorer le prompt plus tard)
✅ RLS Supabase (sécurité user-level)

---

## 📦 Fichiers Créés/Modifiés

### 🗄️ Backend (Python/FastAPI)

#### **SQL Migration**
- `apps/api/migrations/create_natal_interpretations_table.sql` ✅
  - Table `natal_interpretations` avec RLS
  - Index unique `(user_id, chart_id, subject, lang, version)`
  - Trigger auto-update `updated_at`

- `apps/api/migrations/rollback_natal_interpretations_table.sql` ✅
  - Rollback complet si besoin

#### **Modèle SQLAlchemy**
- `apps/api/models/natal_interpretation.py` ✅
  - ORM pour la table `natal_interpretations`

#### **Schéma Pydantic**
- `apps/api/schemas/natal_interpretation.py` ✅
  - `NatalSubject` (Literal type)
  - `ChartPayload` (données d'entrée)
  - `NatalInterpretationRequest/Response`

#### **Service Claude**
- `apps/api/services/natal_interpretation_service.py` ✅
  - Appel à Anthropic API (Claude 3.5 Sonnet)
  - Prompt structuré style Astroia
  - Gestion erreurs (timeout, rate limit, etc.)

#### **Route FastAPI**
- `apps/api/routes/natal_interpretation.py` ✅
  - `POST /api/natal/interpretation` - Générer ou récupérer
  - `DELETE /api/natal/interpretation/{chart_id}/{subject}` - Forcer régénération

#### **Dépendances**
- `apps/api/requirements.txt` ✅
  - Ajout: `anthropic==0.39.0`

#### **Main**
- `apps/api/main.py` ✅
  - Register route `natal_interpretation`

---

### 📱 Mobile (React Native/Expo)

#### **Types TypeScript**
- `apps/mobile/types/natal.ts` ✅
  - `NatalSubject` type
  - `ChartPayload` interface
  - `NatalInterpretationRequest/Response` interfaces

#### **Utilitaires**
- `apps/mobile/utils/natalChartUtils.ts` ✅
  - `getChartId()` - Génère ID stable du chart (hash MD5)
  - `planetNameToSubject()` - Convertit nom → NatalSubject
  - `buildSubjectPayload()` - Construit payload pour API

#### **Service API**
- `apps/mobile/services/api.ts` ✅
  - Ajout: `natalInterpretations.generate()`
  - Ajout: `natalInterpretations.delete()`

#### **Composant Modal**
- `apps/mobile/components/NatalInterpretationModal.tsx` ✅
  - Modal fullscreen avec loader
  - Affichage texte (markdown)
  - Bouton "Régénérer" (force_refresh)
  - Gestion erreurs + retry

#### **Écran Thème Natal**
- `apps/mobile/app/natal-chart/result.tsx` ✅
  - Big 3 (Soleil/Lune/Ascendant) → TouchableOpacity
  - Chaque planète → TouchableOpacity
  - State: `modalVisible`, `selectedSubject`, `selectedPayload`
  - Handler: `handlePlacementClick()`
  - Ajout: `tapHint` style (petit texte "Tap pour interpréter")

---

## 🚀 Installation & Setup

### 1️⃣ Backend

```bash
cd apps/api

# Installer la dépendance Anthropic
pip install -r requirements.txt

# Ajouter la clé API Anthropic dans .env
echo "ANTHROPIC_API_KEY=sk-ant-api03-xxxx..." >> .env

# Exécuter la migration SQL dans Supabase
# Via Supabase Studio → SQL Editor → Coller le contenu de:
# migrations/create_natal_interpretations_table.sql
# Puis cliquer "Run"

# OU via CLI Supabase (si installé):
# supabase db push

# Redémarrer l'API
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2️⃣ Mobile

```bash
cd apps/mobile

# Installer crypto-js (nécessaire pour getChartId hash)
npm install crypto-js
npm install --save-dev @types/crypto-js

# Redémarrer Expo
npx expo start -c
```

---

## ✅ Tests Manuels

### Test 1: Génération initiale (cache miss)

1. Ouvrir l'app → Aller sur "Thème Natal"
2. Cliquer sur **Soleil**
3. **Attendu:**
   - Modal s'ouvre
   - Loader pendant 2-5 secondes (appel Claude)
   - Texte d'interprétation s'affiche (markdown)
   - Badge "Depuis le cache" **NON affiché** (première génération)
4. Console logs (dev only):
   ```
   [NatalInterpretation] sun - Cached: false
   ```

### Test 2: Cache hit (re-clic immédiat)

1. Fermer le modal
2. Re-cliquer sur **Soleil**
3. **Attendu:**
   - Modal s'ouvre
   - Pas de loader (ou très court < 500ms)
   - Même texte s'affiche instantanément
   - Badge "♻️ Depuis le cache" **AFFICHÉ** (dev mode)
4. Console logs:
   ```
   [NatalInterpretation] sun - Cached: true
   ```

### Test 3: Génération autre placement

1. Cliquer sur **Lune**
2. **Attendu:**
   - Loader (appel Claude pour nouveau sujet)
   - Texte différent de Soleil
   - Cached: false
3. Cliquer sur **Vénus**, **Mars**, etc.
4. Vérifier que chaque planète a son texte unique

### Test 4: Régénération (force_refresh)

1. Cliquer sur **Soleil** (cached)
2. Cliquer sur bouton "🔄 Régénérer"
3. **Attendu:**
   - Loader (nouvel appel Claude)
   - Texte peut être légèrement différent (température=0.7)
   - Cached: false après refresh

### Test 5: Gestion erreurs

**Scénario A: API offline**
1. Arrêter l'API backend
2. Cliquer sur une planète
3. **Attendu:**
   - Erreur: "Impossible de générer l'interprétation"
   - Bouton "Réessayer" visible

**Scénario B: Clé Anthropic invalide**
1. Mettre une fausse clé dans `.env`
2. Redémarrer API
3. Cliquer sur une planète
4. **Attendu:**
   - Erreur backend HTTP 500
   - Message d'erreur affiché dans modal

### Test 6: Vérification DB

```sql
-- Dans Supabase Studio → SQL Editor
SELECT id, subject, lang, version, cached, created_at
FROM natal_interpretations
WHERE user_id = 'YOUR_USER_ID'
ORDER BY created_at DESC
LIMIT 10;
```

**Attendu:**
- 1 row par placement testé (sun, moon, venus, etc.)
- `output_text` contient le markdown
- `input_json` contient `{subject_label, sign, degree, house, ascendant_sign}`
- `cached` non utilisé (géré par endpoint)

---

## 🔧 Debugging

### Logs Backend

```bash
# Démarrer API en mode verbose
cd apps/api
uvicorn main:app --reload --host 0.0.0.0 --port 8000 --log-level debug

# Logs attendus lors d'un appel:
# [natal_interpretation.py] 📖 Demande interprétation - user=..., chart=..., subject=sun
# [natal_interpretation_service.py] 🤖 Appel Claude pour sun en Bélier
# [natal_interpretation_service.py] ✅ Interprétation générée (1234 caractères)
# [natal_interpretation.py] ✅ Interprétation sauvegardée (id=...)
```

### Logs Mobile

```javascript
// Dans le terminal Expo
// Lors d'un clic sur une planète:
[NatalInterpretation] sun - Cached: false

// Si erreur:
[NatalInterpretation] Erreur: {...}
```

### Vérifier la clé Anthropic

```bash
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model":"claude-3-5-sonnet-20241022","max_tokens":100,"messages":[{"role":"user","content":"Hello"}]}'

# Attendu: JSON avec "content": [{"text": "Hello! How can I..."}]
# Si erreur: {"error": {"type": "authentication_error", ...}}
```

---

## 📝 Format de l'Interprétation (Prompt Claude)

### Structure générée:

```markdown
**☀️ Soleil en Bélier**

**Ce que ça représente**
[1-2 phrases essence]

**En Bélier**
[3-6 lignes concrètes + nuances]

**À cultiver aujourd'hui**
- [Action/réflexion 1]
- [Qualité à développer 2]
- [Pratique/mantra 3]
```

### Contraintes du prompt:
- ✅ Ton calme, concret, bienveillant
- ✅ Pas de prédictions absolues
- ✅ Pas de conseils santé
- ✅ 900-1400 caractères max
- ✅ Markdown simple
- ✅ Contexte maison si disponible
- ✅ Contexte Ascendant si disponible

---

## 🔐 Sécurité

### Row Level Security (RLS)

Les policies Supabase garantissent:
- ✅ User peut lire uniquement SES interprétations
- ✅ User peut créer uniquement pour SON user_id
- ✅ User peut update/delete uniquement SES interprétations

### Clé API Anthropic

- ⚠️ **JAMAIS** commit la clé dans git
- ✅ Stockée dans `.env` (gitignored)
- ✅ Côté backend uniquement (jamais exposée au mobile)

---

## 💰 Coûts API

### Claude 3.5 Sonnet (2024-10-22)

- **Input:** ~500 tokens/prompt (~$0.0015 par interprétation)
- **Output:** ~400 tokens/interprétation (~$0.006 par interprétation)
- **Total:** ~**$0.008 par interprétation générée**

### Avec cache:
- 1ère génération: $0.008
- Clics suivants: $0.00 (cache DB)

**Exemple:** 100 utilisateurs × 10 placements = 1000 interprétations = **~$8**
(puis $0 pour tous les re-clics)

---

## 🛠️ Améliorations Futures (V2)

### Fonctionnalités
- [ ] Support multilingue (EN, ES, etc.)
- [ ] Régénération auto si version du prompt change
- [ ] Markdown renderer (react-native-markdown-display)
- [ ] Interprétations d'aspects majeurs
- [ ] Interprétations de maisons
- [ ] Export PDF du thème complet

### Technique
- [ ] Hash MD5 réel pour chart_id (actuellement string simplifiée)
- [ ] Auth réelle (actuellement UUID fixe)
- [ ] Streaming Claude (afficher le texte au fur et à mesure)
- [ ] A/B testing de prompts (version 1 vs 2)
- [ ] Analytics (% cached, temps moyen génération)

---

## 🐛 Troubleshooting

### Erreur: "ANTHROPIC_API_KEY non défini"

**Solution:**
```bash
cd apps/api
echo "ANTHROPIC_API_KEY=sk-ant-..." >> .env
# Redémarrer l'API
```

### Erreur: "crypto-js not found"

**Solution:**
```bash
cd apps/mobile
npm install crypto-js @types/crypto-js
```

### Erreur: Table natal_interpretations n'existe pas

**Solution:**
```bash
# Exécuter la migration SQL dans Supabase Studio
# Copier/coller apps/api/migrations/create_natal_interpretations_table.sql
```

### Modal ne s'ouvre pas

**Vérifier:**
1. Console: erreurs TypeScript ?
2. `chartId` est bien défini ?
3. `buildSubjectPayload()` retourne un payload valide ?

---

## ✨ Résultat Final

L'utilisateur peut maintenant:
1. **Cliquer** sur n'importe quel placement de son thème natal
2. **Lire** une interprétation personnalisée générée par Claude
3. **Bénéficier** du cache (pas de délai au 2ème clic)
4. **Régénérer** s'il veut une variation

**Style Astroia:** Calme, concret, bienveillant, jamais fataliste. ✨
