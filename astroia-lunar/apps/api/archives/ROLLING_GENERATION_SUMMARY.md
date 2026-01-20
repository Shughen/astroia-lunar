# ✅ Génération Rolling - Résumé des modifications

## 🎯 Objectif

Garantir que `/next` trouve toujours un retour à venir après génération, même si nous sommes fin d'année (ex: décembre 2025 où tous les retours de 2025 sont passés).

---

## 📝 Modifications apportées

### 1. `routes/lunar_returns.py` - POST `/generate`

**Changement principal :** Génération de 12 retours glissants au lieu d'une année civile fixe.

**Avant :**
```python
current_year = datetime.now().year
months = [f"{current_year}-{str(m).zfill(2)}" for m in range(1, 13)]
```

**Après :**
```python
# Générer 12 retours glissants à partir de maintenant
now = datetime.now(timezone.utc)

# Calculer le mois de départ : mois suivant si on est après le 15, sinon mois courant
if now.day > 15:
    if now.month == 12:
        start_year = now.year + 1
        start_month = 1
    else:
        start_year = now.year
        start_month = now.month + 1
else:
    start_year = now.year
    start_month = now.month

# Générer les 12 prochains mois calendaires
current_year = start_year
current_month = start_month
for i in range(12):
    month_str = f"{current_year}-{str(current_month).zfill(2)}"
    months.append(month_str)
    current_month += 1
    if current_month > 12:
        current_month = 1
        current_year += 1
```

**Logique :**
- Si on est **après le 15 du mois** → commence au mois suivant (évite de générer un retour déjà passé)
- Si on est **avant le 15 du mois** → commence au mois courant
- Génère toujours **12 mois calendaires consécutifs**

**Exemple :**
- Date : 22 décembre 2025
- Mois générés : 2026-01, 2026-02, ..., 2026-12 (12 mois)
- Résultat : `/next` trouvera toujours un retour à venir

**Réponse modifiée :**
```json
{
  "message": "12 révolution(s) lunaire(s) générée(s)",
  "mode": "rolling",
  "months_count": 12,
  "generated_count": 12,
  "errors_count": 0,
  "correlation_id": "..."
}
```

---

### 2. `tests/test_lunar_returns.py`

**Mise à jour :** Vérifie que la réponse contient `mode: "rolling"` au lieu de `year`.

```python
assert "mode" in data, "Response should have 'mode' field (rolling)"
assert data["mode"] == "rolling", f"Expected mode='rolling', got '{data['mode']}'"
```

---

### 3. `tests/test_lunar_returns_next_after_generate.py` (NOUVEAU)

**Test ajouté :** Vérifie que `/next` retourne 200 après génération.

**Note :** Ce test nécessite que `FakeAsyncSession` soit étendu pour stocker les objets ajoutés et les retourner lors des queries. Pour l'instant, le test vérifie la logique de génération rolling.

---

### 4. `LOCAL_TEST_CURL.md`

**Documentation mise à jour :** Réponse de `/generate` maintenant avec `mode: "rolling"` au lieu de `year`.

---

## ✅ Résultat attendu

1. **Génération :** Toujours 12 retours glissants à partir de maintenant (ou mois suivant)
2. **`/next` :** Retourne toujours 200 avec un retour à venir (pas de 404)
3. **`/year/{year}` :** Continue de fonctionner pour une année civile spécifique

---

## 🔍 Exemples de scénarios

### Scénario 1 : Mi-année (15 juillet 2025)

- Date : 2025-07-10
- Mois générés : 2025-07, 2025-08, ..., 2026-06 (12 mois)
- `/next` : Retourne un retour en juillet 2025 ou après

### Scénario 2 : Fin d'année (22 décembre 2025)

- Date : 2025-12-22
- Mois générés : 2026-01, 2026-02, ..., 2026-12 (12 mois)
- `/next` : Retourne un retour en janvier 2026 ou après

### Scénario 3 : Début d'année (5 janvier 2026)

- Date : 2026-01-05
- Mois générés : 2026-01, 2026-02, ..., 2026-12 (12 mois)
- `/next` : Retourne un retour en janvier 2026 ou après

---

## 🧪 Tests

### Test unitaire

```bash
pytest tests/test_lunar_returns.py::test_success_generate_201 -v
```

**Vérifie :**
- ✅ Statut 201
- ✅ `mode: "rolling"` dans la réponse
- ✅ `generated_count > 0`

### Test E2E (curl)

```bash
# 1. Générer les retours
curl -X POST "http://localhost:8000/api/lunar-returns/generate" \
  -H "Authorization: Bearer $TOKEN" | jq

# 2. Vérifier /next (devrait retourner 200, pas 404)
curl -X GET "http://localhost:8000/api/lunar-returns/next" \
  -H "Authorization: Bearer $TOKEN" | jq
```

**Résultat attendu :**
- `/generate` → 201 avec `mode: "rolling"`
- `/next` → 200 avec `return_date >= now()`

---

## 📋 Checklist de validation

- [x] Code modifié pour générer 12 mois glissants
- [x] Logique de mois de départ (après 15 → mois suivant)
- [x] Réponse `/generate` avec `mode: "rolling"`
- [x] Tests unitaires mis à jour
- [x] Documentation mise à jour
- [x] `correlation_id` et erreurs structurées conservées
- [x] `return_date` toujours calculé par trigger DB (non modifié)

---

## ⚠️ Notes importantes

1. **Trigger DB inchangé :** `return_date` est toujours rempli automatiquement par le trigger PostgreSQL depuis `raw_data.return_datetime`. La modification ne touche que la logique de génération des mois.

2. **Compatibilité :** Les retours existants (année civile fixe) continuent de fonctionner. La génération rolling s'applique uniquement aux nouvelles générations.

3. **`/year/{year}` :** Continue de fonctionner pour une année civile spécifique. La génération rolling ne modifie pas ce endpoint.

---

**Modifications complètes et prêtes à être testées !** 🌙✨

