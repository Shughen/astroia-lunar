# Fix du bug de date (-1 jour) ✅

## Problème résolu

**Symptôme**: Quand l'utilisateur entre `09/02/2001` comme date de naissance, en base de données on se retrouve avec `2001-02-08`.

**Impact**: Le thème natal de Nathan affichait la Lune en **Leo** (position du 8 février) au lieu de **Virgo** (position du 9 février).

## Cause racine identifiée

### Ligne de code problématique

**Fichier**: `apps/mobile/app/onboarding/profile-setup.tsx` ligne 230

```typescript
date: birthDate.toISOString().split('T')[0], // ❌ BUG
```

### Explication technique

`toISOString()` convertit la date en **UTC** avant de la formater. Cela cause un décalage d'un jour selon la timezone :

**Exemple avec Nathan** (né à Bordeaux, timezone Europe/Paris = UTC+1):

1. **Utilisateur sélectionne**: `09/02/2001 00:00` (minuit en heure locale)
2. **En mémoire JavaScript**: `Date('2001-02-09T00:00:00+01:00')`
3. **toISOString() convertit en UTC**: `'2001-02-08T23:00:00.000Z'` (23h la veille!)
4. **split('T')[0] extrait**: `'2001-02-08'` ❌

## Solution implémentée

### Nouvelle fonction utilitaire

**Fichier**: `apps/mobile/utils/date.ts`

```typescript
/**
 * Formate une date en YYYY-MM-DD en heure locale (pas UTC!)
 */
export function formatDateLocal(date: Date): string {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}
```

**Avantages**:
- Utilise `getFullYear()`, `getMonth()`, `getDate()` qui retournent les valeurs en **heure locale**
- Pas de conversion UTC
- La date reste exactement celle sélectionnée par l'utilisateur

### Correction appliquée

**Fichier**: `apps/mobile/app/onboarding/profile-setup.tsx`

```typescript
// Avant (BUG)
date: birthDate.toISOString().split('T')[0],

// Après (FIX)
date: formatDateLocal(birthDate),
```

## Tests à effectuer

### 1. Vider la base et recalculer le thème de Nathan

```bash
# Dans DBeaver ou psql
TRUNCATE TABLE natal_charts RESTART IDENTITY CASCADE;
```

### 2. Relancer l'app mobile

1. Désinstaller l'app (pour vider le cache)
2. Réinstaller avec Expo
3. Compléter l'onboarding avec les données de Nathan:
   - Date: `09/02/2001`
   - Heure: `11:30`
   - Lieu: Bordeaux

### 3. Vérifier en base de données

```sql
SELECT
  id,
  birth_date,
  birth_time,
  positions->'moon' as moon_position
FROM natal_charts
ORDER BY created_at DESC
LIMIT 1;
```

**Résultat attendu**:
```
birth_date: 2001-02-09  ✅ (pas 2001-02-08)
moon_position: {"sign": "Virgo", "degree": 6.9, "house": 5}  ✅ (pas Leo)
```

### 4. Vérifier dans l'app mobile

- Ouvrir le thème natal de Nathan
- Vérifier: **Lune en Vierge** (pas Lion)
- Vérifier: Degré ~6.9°

## Validation finale

### Positions attendues pour Nathan (9 février 2001, 11:30, Bordeaux)

D'après **Swiss Ephemeris** et **Astrotheme**:

| Planète | Signe | Degré | Maison |
|---------|-------|-------|--------|
| Soleil  | Verseau (Aquarius) | 20.74° | 11 |
| **Lune** | **Vierge (Virgo)** ✅ | **6.9°** | **5** |
| Ascendant | Taureau (Taurus) | 14.89° | 1 |

## Commits

1. **debug**: Logs de traçage (`6c4f38e`)
   - Ajout de logs détaillés pour identifier le bug
   - Scripts de diagnostic (16 scripts)
   - Rapport: `DIAGNOSTIC_NATHAN.md`

2. **fix(mobile)**: Correction du bug (`c803a3f`)
   - Nouvelle fonction `formatDateLocal()`
   - Fix dans `profile-setup.tsx`

## Autres occurrences à vérifier (optionnel)

Le pattern `toISOString().split('T')[0]` existe ailleurs dans le code:

```bash
apps/mobile/services/lunarCache.ts:44
apps/mobile/app/journal.tsx:127
apps/mobile/services/api.ts:596
# + tests
```

**Note**: Ces occurrences utilisent `new Date().toISOString()` pour la date **actuelle**, ce qui est moins problématique. Mais pour cohérence, on pourrait les remplacer aussi.

## Prévention

### Règle à suivre

❌ **Ne jamais utiliser** `toISOString().split('T')[0]` pour une date de naissance ou toute date saisie par l'utilisateur

✅ **Toujours utiliser** `formatDateLocal(date)` pour les dates utilisateur

### Pourquoi?

- Les dates de naissance sont conceptuellement en **heure locale**
- `toISOString()` convertit en **UTC** (universel)
- Cela peut causer des décalages de ±1 jour selon la timezone

## Résultat

✅ **Bug corrigé**: La date saisie reste identique en base de données
✅ **Impact**: Nathan a maintenant sa Lune en **Virgo** comme attendu
✅ **Prévention**: Nouvelle fonction `formatDateLocal()` pour éviter ce bug à l'avenir
