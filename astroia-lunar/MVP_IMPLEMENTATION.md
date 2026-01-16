# MVP Implementation - Astroia Lunar

**Statut :** Phase 1 terminée ✅ | Phase 2 en cours 🚧 | Phase 3 à faire ⏳

---

## ✅ Phase 1 Terminée (Quick Wins)

### Chantier 1A : Journal Mobile → Backend API ✅
**Commits :** `a7878cf`

**Réalisé :**
- Ajout de 4 méthodes API dans `apps/mobile/services/api.ts` :
  - `journal.createEntry(date, note, mood?, month?)`
  - `journal.getEntries(params?)`
  - `journal.getTodayEntry()`
  - `journal.deleteEntry(entryId)`
- Réécriture de `apps/mobile/services/journalService.ts` : AsyncStorage → API backend
- Adaptation de `apps/mobile/app/journal.tsx` avec gestion d'erreurs réseau
- Mapping : frontend `text` → backend `note`, `moonContext` par défaut

**Validation :**
```bash
# TypeScript compile
cd apps/mobile && npx tsc --noEmit

# Backend tests
cd apps/api && pytest tests/test_journal.py -v
# → 11 tests doivent passer
```

---

### Chantier 1B : Home Layout Lunar-Centric ✅
**Commits :** `f8e0fca`

**Réalisé :**
- Suppression du bouton "Rapport Mensuel" du menu grid (doublon avec CurrentLunarCard)
- Menu simplifié : Thème natal + Réglages uniquement
- CurrentLunarCard reste en position HERO avec CTA "Voir le rapport mensuel"

**Fichier modifié :** `apps/mobile/app/index.tsx`

---

### Chantier 1C : Nettoyage Hors MVP ✅
**Commits :** `55162c6`

**Réalisé :**
- **Mobile supprimés :** `app/cycle/`, `app/calendar/`, `app/timeline.tsx`, `app/lunar/index.tsx`
- **Backend supprimés :** `routes/calendar.py`, `services/calendar_services.py`
- **Mise à jour :** `app/_layout.tsx`, `main.py`, `services/api.ts`
- **Impact :** -2962 lignes de code obsolètes

**Validation :**
```bash
cd apps/mobile && npx tsc --noEmit
# → Pas d'erreurs d'imports manquants
```

---

## 🚧 Phase 2 : Refinements (2-3 jours)

### Chantier 2 : Valider Format Rapport Lunaire
**Impact :** MEDIUM | **Effort :** 1 jour | **Statut :** 🔴 À faire

**Objectif :**
Valider que les rapports lunaires respectent le format MVP (1 page, 3 sections, ton factuel non ésotérique).

**Fichiers critiques :**
1. `apps/api/routes/lunar.py` (lignes ~300-500)
   - Endpoint : `POST /api/lunar/return/report`
   - Vérifier structure réponse : 3 sections (Climat du mois, Périodes clés, Points d'attention)
   - Ajuster prompts IA si nécessaire pour ton "factuel, senior"

2. `apps/mobile/app/lunar/report.tsx`
   - Vérifier affichage correspond au format backend
   - Ajouter rendering markdown si besoin (MarkdownText.tsx existe déjà)

**Méthode de validation :**
1. Générer 5 rapports échantillons pour différents mois
2. Audit manuel : clarté, concision, actionnable ?
3. Vérifier absence jargon ésotérique ("énergies", "vibrations", etc.)
4. Ajuster prompts IA si besoin

**Tests API :**
```bash
# Tester génération rapport
curl -X POST http://localhost:8000/api/lunar/return/report \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1990-05-15",
    "birth_time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris",
    "date": "2026-01-16",
    "month": "2026-01"
  }'

# Vérifier structure réponse contient bien 3 sections
```

**Critères de succès :**
- [ ] Rapport contient exactement 3 sections identifiables
- [ ] Ton factuel, non ésotérique (≤ 2 occurrences de mots ésotériques tolérés)
- [ ] Longueur : 300-800 mots par rapport
- [ ] Contenu actionnable (dates clés, recommandations concrètes)
- [ ] Affichage mobile correct avec markdown

---

### Chantier 3 : Filtrage Backend Transits Majeurs
**Impact :** MEDIUM | **Effort :** 1 jour | **Statut :** 🔴 À faire

**Objectif :**
Déplacer le filtrage des transits majeurs du client vers le backend.

**Situation actuelle :**
`TransitsWidget.tsx` filtre déjà côté client (conjonction, opposition, carré, trigone uniquement).

**Fichiers à modifier :**

1. **`apps/api/routes/transits.py`** (~30 lignes)
   ```python
   # Ajouter paramètre major_only à GET /transits/overview/{user_id}/{month}
   # Filtrer aspects :
   - Garder : conjunction, opposition, square, trine
   - Exclure : sextile, semi-sextile, quincunx, etc.
   # Filtrer corps :
   - Garder : Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto
   - Exclure : Nodes, Chiron, Lilith, astéroïdes
   ```

2. **`apps/mobile/components/TransitsWidget.tsx`** (~20 lignes simplifiées)
   - Utiliser filtrage backend via param `?major_only=true`
   - Supprimer logique de filtrage client

**Validation :**
```bash
# Test backend avec filtrage
curl "http://localhost:8000/api/transits/overview/USER_ID/2026-01?major_only=true" \
  -H "Authorization: Bearer TOKEN"
# Doit retourner <= 10 aspects (seulement majeurs)

# Test sans filtrage (pour comparaison)
curl "http://localhost:8000/api/transits/overview/USER_ID/2026-01" \
  -H "Authorization: Bearer TOKEN"
# Doit retourner tous les aspects
```

**Critères de succès :**
- [ ] Backend accepte param `?major_only=true`
- [ ] Filtrage correct : seulement 4 aspects majeurs + 10 corps principaux
- [ ] TransitsWidget utilise le param backend
- [ ] Performance identique ou améliorée
- [ ] Widget affiche <= 3 transits sur Home

---

### Chantier 4 : Fiabilité VoC Status
**Impact :** LOW | **Effort :** 0.5 jour | **Statut :** 🔴 À faire

**Objectif :**
Optimiser cache et retry logic pour VoC (Void of Course).

**Fichiers à vérifier :**

1. **`apps/api/routes/lunar.py`**
   - Vérifier cache TTL sur `GET /api/lunar/voc/status` (5 min recommandé)
   - S'assurer que `now`, `next`, `upcoming` sont tous calculés
   - Code actuel :
     ```python
     @router.get("/api/lunar/voc/status")
     async def get_voc_status(...):
         # Vérifier que le cache est correctement configuré
     ```

2. **`apps/mobile/components/VocWidget.tsx`** (~10 lignes)
   - Ajouter retry logic sur erreur réseau (3 tentatives, exponential backoff)
   - Auto-refresh déjà implémenté (5 min)
   - Ajouter fallback si API down (afficher données cache + warning)

**Exemple retry logic :**
```typescript
const fetchVocWithRetry = async (retries = 3, delay = 1000) => {
  for (let i = 0; i < retries; i++) {
    try {
      return await lunaPack.getCurrentVoc();
    } catch (error) {
      if (i === retries - 1) throw error;
      await new Promise(resolve => setTimeout(resolve, delay * Math.pow(2, i)));
    }
  }
};
```

**Validation :**
```bash
# Test cache backend
curl http://localhost:8000/api/lunar/voc/status \
  -H "Authorization: Bearer TOKEN"
# Appeler 2x rapidement → 2ème doit être instantanée (cache)

# Test widget mobile
# Simuler : couper réseau → VocWidget doit afficher warning + cache
```

**Critères de succès :**
- [ ] VocWidget charge en < 1s (cache backend)
- [ ] Auto-refresh fonctionne (toutes les 5 min)
- [ ] Erreurs réseau ne bloquent pas l'affichage (retry + fallback)
- [ ] Cache backend configuré à 5 min TTL

---

## ⏳ Phase 3 : Quality Assurance (1-2 jours)

### Chantier 5 : Tests d'Intégration
**Impact :** HIGH | **Effort :** 1 jour | **Statut :** 🔴 À faire

**Objectif :**
Valider les 5 parcours MVP critiques.

**Scénarios de test manuel :**

#### 1. Onboarding → Home
- [ ] Inscription → profil → thème natal → Home charge
- [ ] CurrentLunarCard affiche mois actuel
- [ ] Tous widgets chargent en < 3s

#### 2. Journal
- [ ] Home → JournalPrompt → Créer entrée
- [ ] Entrée sauvegardée en DB (vérifier avec curl)
- [ ] Widget affiche ✅ "Aujourd'hui"
- [ ] Historique charge depuis API

#### 3. VoC
- [ ] Widget Home affiche statut correct
- [ ] "Prochaine fenêtre" avec date/heure
- [ ] Auto-refresh après 5 min

#### 4. Transits
- [ ] Widget affiche top 3 aspects
- [ ] Symboles corrects (◎ ◉ ■ ▲)
- [ ] Navigation vers /transits/overview

#### 5. Rapport Lunaire
- [ ] Home → CurrentLunarCard → "Voir rapport"
- [ ] Rapport charge avec 3 sections
- [ ] Contenu clair et actionnable

**Tests backend à créer :**

1. **`apps/api/tests/test_journal.py`** ✅ (existe déjà)
   ```bash
   cd apps/api
   pytest tests/test_journal.py -v
   # → 11 tests doivent passer
   ```

2. **`apps/api/tests/test_transits_filtering.py`** (nouveau)
   ```python
   def test_major_only_filter():
       # Vérifier que ?major_only=true retourne seulement 4 aspects

   def test_planetary_bodies_only():
       # Vérifier exclusion nodes/chiron/lilith
   ```

**Validation finale :**
```bash
# Backend
cd apps/api
pytest -q                                # Tous tests passent
pytest tests/test_journal.py -v         # 11 tests OK
pytest tests/test_transits_filtering.py -v

# Mobile
cd apps/mobile
npx tsc --noEmit                        # Pas d'erreurs TS
npm run lint                             # Pas de warnings critiques
```

**Critères de succès :**
- [ ] 5 parcours testés manuellement OK
- [ ] Tous les tests backend passent
- [ ] Aucune erreur TypeScript
- [ ] Performance : chaque écran charge en < 3s

---

### Chantier 6 : Documentation
**Impact :** MEDIUM | **Effort :** 0.5 jour | **Statut :** 🔴 À faire

**Objectif :**
Documenter le MVP pour utilisateurs et développeurs.

**Fichiers à créer/mettre à jour :**

#### 1. **`QUICKSTART_MVP.md`** (nouveau)
```markdown
# Démarrage Rapide MVP

## Pour Utilisateurs
- Fonctionnalités principales
- Parcours utilisateur
- Screenshots clés

## Pour Développeurs
- Setup environnement
- Lancer API + Mobile
- Tests
```

#### 2. **`docs/MVP_API.md`** (nouveau)
```markdown
# API MVP - Documentation

## Endpoints Journal
- POST /api/journal/entry
- GET /api/journal/entries
- GET /api/journal/today
- DELETE /api/journal/entry/{id}

## Endpoints Lunar
- GET /api/lunar-returns/current
- GET /api/lunar/voc/status
- POST /api/lunar/return/report

## Endpoints Transits
- GET /api/transits/overview/{user_id}/{month}?major_only=true
```

#### 3. **Mettre à jour `README.md`**
- Ajouter section MVP avec lien vers QUICKSTART_MVP.md
- Mettre à jour statut des features (terminées/en cours)
- Ajouter badges de statut si pertinent

**Critères de succès :**
- [ ] QUICKSTART_MVP.md permet à un nouveau dev de démarrer en < 15 min
- [ ] MVP_API.md documente tous les endpoints MVP avec exemples curl
- [ ] README.md à jour avec statut MVP

---

## 📊 Definition of Done MVP

Le MVP est considéré shippable quand :

- [x] Backend journal API implémenté et testé
- [x] Mobile journal connecté au backend
- [x] Home est "lunar-centric"
- [x] VocWidget fonctionnel
- [x] TransitsWidget fonctionnel
- [x] Cleanup complet
- [ ] Format rapport lunaire validé (Chantier 2)
- [ ] Filtrage transits backend (Chantier 3)
- [ ] VoC fiabilité optimisée (Chantier 4)
- [ ] 5 parcours d'intégration validés (Chantier 5)
- [ ] Documentation complète (Chantier 6)

**Estimation totale restante :** 3-4 jours développeur effectifs

---

## 🔧 Commandes Utiles

### Backend
```bash
cd apps/api

# Lancer serveur
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Tests
pytest -q                                # Tous tests
pytest tests/test_journal.py -v         # Tests journal
pytest tests/test_transits_filtering.py -v  # Tests transits (à créer)

# Sanity check
python scripts/schema_sanity_check.py
```

### Mobile
```bash
cd apps/mobile

# TypeScript check
npx tsc --noEmit

# Linter
npm run lint

# Démarrer app
npm start
```

### Git
```bash
# Statut
git status --short

# Commit format
git commit -m "feat(scope): description

Détails...

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## 📝 Notes Importantes

### Règles strictes (CLAUDE.md)
- ❌ Ne jamais modifier `.env`
- ❌ Ne jamais afficher/commiter de secrets
- ✅ Un changement = un commit
- ✅ Priorité : correctif minimal, tests, puis refacto

### Zones interdites
- Ne jamais toucher : `apps/mobile` sauf demande explicite (déjà respecté)
- Ne jamais modifier : `.env`, `**/*.key`, `**/secrets*`

### Backend tests avant commit
```bash
cd apps/api && pytest -q
# Doit passer avant tout commit backend
```

---

## 🎯 Ordre d'Exécution Recommandé

### Semaine 1 (Phase 2 + partie Phase 3)
- **Jour 1 :** Chantier 2 (Rapport lunaire)
- **Jour 2 :** Chantier 3 (Transit filtering)
- **Jour 3 :** Chantier 4 (VoC fiabilité) + Tests manuels

### Semaine 2 (Finalisation Phase 3)
- **Jour 4 :** Chantier 5 (Tests intégration)
- **Jour 5 :** Chantier 6 (Documentation) + Fixes finaux

**Deliverable final :** MVP poli, testé, documenté

---

## 📞 Pour Continuer

**Si tu fais `/clear` et veux reprendre :**

1. Ouvre ce fichier : `MVP_IMPLEMENTATION.md`
2. Dis-moi : "Continue avec le Chantier N du MVP_IMPLEMENTATION.md"
3. Je lirai ce fichier et continuerai exactement où on s'est arrêté

**Prochain chantier recommandé :** Chantier 2 (Valider Format Rapport Lunaire)
