# Fix Pack: Auth, Calendar, Transits - Récapitulatif

## Date: 2025-01-XX
## Branche: `fix/bugpack-auth-calendar-transits`

## Fichiers modifiés

### 1. `apps/mobile/services/api.ts`
**Problème**: Exports `calendar` et `transits` manquants → crash "Cannot read property 'getMonth'/'getOverview' of undefined"

**Corrections**:
- ✅ Ajouté export `calendar` avec fonction `getMonth(year, month, latitude?, longitude?, timezone?)`
  - Appelle `GET /api/calendar/month?year={year}&month={month}`
- ✅ Ajouté export `transits` avec fonction `getOverview(userId, month, token?)`
  - Appelle `GET /api/transits/overview/{userId}/{month}`
  - Le token est géré automatiquement par l'intercepteur axios

---

### 2. `apps/mobile/app/debug/selftest.tsx`
**Problème**: Erreurs 422/401 mal diagnostiquées, format données incorrect

**Corrections**:
- ✅ Corrigé format `birth_latitude` et `birth_longitude` : string → float
- ✅ Ajouté logs détaillés pour Register/Login :
  - Payload envoyé (password masqué)
  - Endpoint appelé
  - Status code et body d'erreur
- ✅ Amélioré affichage erreurs :
  - 422 : Détails validation Pydantic formatés
  - 401 : Message "Unauthorized" avec détails
  - Affichage JSON structuré dans l'UI

---

### 3. `apps/mobile/app/calendar/month.tsx`
**Problème**: Crash "Cannot read property 'getMonth' of undefined" si `currentDate` invalide

**Corrections**:
- ✅ Ajouté guards sur `currentDate` :
  - Vérification que c'est une Date valide avant utilisation
  - Fallback UI si date invalide
- ✅ Validation `year`/`month` avant appel API
- ✅ Gestion erreurs changement de mois
- ✅ Initialisation sûre avec `useState(() => new Date())`

---

### 4. `apps/mobile/app/transits/overview.tsx`
**Problème**: Hardcode `userId=1` et `'fake_token'`, crash si `transitsData` undefined

**Corrections**:
- ✅ Remplacé hardcode par valeurs du store `useAuthStore`
- ✅ Ajouté support `DEV_AUTH_BYPASS` (récupère userId depuis env)
- ✅ Ajouté guards sur `transitsData` avant accès propriétés
- ✅ Vérification authentification avant chargement
- ✅ Fallback UI si données non disponibles

---

## Instructions pour tester

### Flow 1: Auth Self-Test (diagnostic 422/401)

1. Lancer l'app mobile : `cd apps/mobile && npx expo start`
2. Naviguer vers `/debug/selftest`
3. Cliquer sur "Run Auth E2E"
4. **Vérifier** :
   - ✅ Health Check passe
   - ✅ Register : Si 422, voir détails validation dans l'UI et console
   - ✅ Login : Si 401, voir message "Unauthorized" avec détails
   - ✅ Les logs dans console montrent payload (password masqué) et endpoint

**Si Register retourne 422** :
- Vérifier dans les logs que `birth_latitude` et `birth_longitude` sont des floats
- Vérifier le format des autres champs (birth_date, birth_time)
- Si nécessaire, vérifier côté API que le schéma `UserRegister` accepte ces formats

---

### Flow 2: Calendrier Lunaire (fix crash)

1. Naviguer vers `/calendar/month`
2. **Vérifier** :
   - ✅ Pas de crash au chargement
   - ✅ Calendrier s'affiche ou message d'erreur clair
   - ✅ Navigation mois précédent/suivant fonctionne
   - ✅ Si erreur API, bouton "Réessayer" visible

**Si crash persiste** :
- Vérifier dans les logs console que `currentDate` est valide
- Vérifier que l'API `/api/calendar/month?year=...&month=...` répond correctement

---

### Flow 3: Transits Overview (fix crash + auth)

1. S'assurer d'être connecté (ou activer `DEV_AUTH_BYPASS=true`)
2. Naviguer vers `/transits/overview`
3. **Vérifier** :
   - ✅ Pas de crash au chargement
   - ✅ Utilise le vrai `userId` du store (pas hardcode)
   - ✅ Transits s'affichent ou message d'erreur clair
   - ✅ Si non authentifié, message "Vous devez être connecté"

**Si crash persiste** :
- Vérifier que `user.id` existe dans le store auth
- Vérifier que l'API `/api/transits/overview/{user_id}/{month}` répond correctement
- Vérifier que le token est bien envoyé (logs intercepteur axios)

---

## Diagnostic bug 422 (Register)

### Hypothèses racines

1. **Format données** : `birth_latitude`/`birth_longitude` envoyés comme strings au lieu de floats
   - ✅ **Corrigé** : Conversion string → float dans `selftest.tsx`

2. **Validation Pydantic** : Le backend rejette certains champs
   - Vérifier dans `apps/api/routes/auth.py` que le schéma `UserRegister` accepte :
     - `birth_date: Optional[str]` (format YYYY-MM-DD)
     - `birth_time: Optional[str]` (format HH:MM)
     - `birth_latitude: Optional[float]`
     - `birth_longitude: Optional[float]`

3. **Champs manquants** : Le backend attend des champs non fournis
   - Vérifier les logs pour voir quels champs sont rejetés

### Patch serveur proposé (si nécessaire)

Si le problème vient du backend, vérifier dans `apps/api/routes/auth.py` :

```python
class UserRegister(BaseModel):
    email: EmailStr
    password: str
    birth_date: Optional[str] = None  # Format YYYY-MM-DD
    birth_time: Optional[str] = None  # Format HH:MM
    birth_latitude: Optional[float] = None  # Float, pas string
    birth_longitude: Optional[float] = None  # Float, pas string
    birth_place_name: Optional[str] = None
    # Note: birth_timezone n'est pas dans le schéma mais envoyé par le frontend
```

Si `birth_timezone` est requis, l'ajouter au schéma ou le retirer du payload frontend.

---

## Validation finale

- [x] Code corrigé
- [x] Types TypeScript respectés (pas d'erreurs lint)
- [x] Guards ajoutés sur tous les accès aux données
- [x] Logs utiles ajoutés (sans secrets)
- [x] Commits atomiques créés (4 commits séparés)

## Prochaines étapes

1. Tester les 3 flows manuels ci-dessus
2. Si bug 422 persiste, vérifier les logs détaillés et ajuster le format des données
3. Si nécessaire, proposer un patch backend pour aligner le schéma Pydantic
4. Vérifier que tous les écrans fonctionnent sans crash

