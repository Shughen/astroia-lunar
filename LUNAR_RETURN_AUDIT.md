# Audit et Correction du Calcul des Révolutions Lunaires

## 📋 Rapport d'Audit

### Problème identifié

Les dates de révolutions lunaires affichées dans la timeline étaient des **placeholders fixes** :
- **Format** : "15 <mois> <année> à 12:00" (ex: "15 janvier 2026 à 12:00")
- **Localisation** : `apps/api/utils/ephemeris_mock.py`, ligne 152 (ancien code)
- **Cause** : Le mock utilisait une date fixe au lieu de calculer le vrai moment où λ_moon(t) = λ_moon_natal

### État actuel (avant correction)

**Fichier** : `apps/api/utils/ephemeris_mock.py`
```python
# Date estimée (15 du mois)
year, month = map(int, target_month.split("-"))
return_datetime = f"{target_month}-15T12:00:00"
```

**Impact** :
- Toutes les révolutions lunaires avaient le même jour du mois (15) et la même heure (12:00)
- Les intervalles entre révolutions n'étaient pas réalistes (~27.3 jours)
- Les dates ne variaient pas d'un mois à l'autre

### Solution implémentée

1. **Nouvelle fonction de calcul** : `find_lunar_return()` dans `apps/api/services/swiss_ephemeris.py`
   - Utilise Swiss Ephemeris (pyswisseph) pour calculer les positions lunaires précises
   - Algorithme en 3 étapes :
     - **Approximation** : utilise le mois sidéral (~27.32 jours) pour estimer la date
     - **Bracket** : scanne avec un pas de 30 min pour trouver un changement de signe de Δ = angleDiff(λ(t), λ_natal)
     - **Refinement** : bisection jusqu'à tolérance de 60 secondes

2. **Helpers ajoutés** :
   - `normalize_angle_360(degree)` : normalise un angle dans [0, 360)
   - `angle_diff_signed(a, b)` : calcule la différence signée dans [-180, 180]

3. **Modification du mock** : `apps/api/utils/ephemeris_mock.py`
   - Utilise maintenant `find_lunar_return()` si Swiss Ephemeris est disponible
   - Fallback sur placeholder si Swiss Ephemeris n'est pas disponible
   - Gère les deux formats de degré : degré dans le signe (0-30) ou longitude absolue (0-360)

### Fichiers modifiés

1. `apps/api/services/swiss_ephemeris.py`
   - Ajout de `normalize_angle_360()`
   - Ajout de `angle_diff_signed()`
   - Ajout de `find_lunar_return()`

2. `apps/api/utils/ephemeris_mock.py`
   - Import de Swiss Ephemeris
   - Modification de `generate_mock_lunar_return()` pour utiliser le calcul réel

### Validation attendue

Après déploiement, vérifier que :
- ✅ Les dates varient d'un mois à l'autre (pas toujours le 15)
- ✅ Les heures varient (pas toujours 12:00)
- ✅ Les intervalles entre révolutions sont ~27.3 jours (±1 jour)
- ✅ La longitude lunaire au moment du retour est proche de la longitude natale (<0.01°)

### Notes techniques

- **Précision** : tolérance de 60 secondes (suffisant pour V1)
- **Performance** : recherche dans une fenêtre de 48h par défaut
- **Dépendances** : nécessite `pyswisseph==2.10.3.2` (déjà dans requirements.txt)
- **Compatibilité** : fonctionne en mode mock (DEV_MOCK_EPHEMERIS=1) et avec l'API réelle

