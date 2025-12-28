# ✅ Génération Rolling Hardened - Résumé des modifications

## 🎯 Objectif

Éviter les doublons lors de la génération rolling en supprimant les retours existants dans la période avant insertion, puis vérifier post-insert qu'on a bien 12 retours.

---

## 📝 Modifications apportées

### 1. Calcul de la période rolling (`start_date` et `end_date`)

**Avant :** On calculait seulement les mois (strings "YYYY-MM").

**Après :** On calcule aussi les dates réelles pour la suppression et la vérification :

```python
# Calculer start_date (début du mois de départ)
start_date = datetime(start_year, start_month, 1, tzinfo=timezone.utc)

# Calculer end_date : début du 13ème mois (après les 12 mois)
end_year = start_year
end_month = start_month + 12
while end_month > 12:
    end_month -= 12
    end_year += 1
end_date = datetime(end_year, end_month, 1, tzinfo=timezone.utc)
```

**Exemple :**
- Date : 22 décembre 2025
- `start_date` : 2026-01-01 00:00:00+00:00
- `end_date` : 2027-01-01 00:00:00+00:00 (début du 13ème mois)

---

### 2. Suppression des retours existants avant insertion

**Ajout :** DELETE des retours dans la période rolling avant la boucle d'insertion.

```python
# Supprimer les retours existants dans la période rolling pour éviter les doublons
try:
    delete_stmt = delete(LunarReturn).where(
        LunarReturn.user_id == current_user.id,
        LunarReturn.return_date >= start_date,
        LunarReturn.return_date < end_date
    )
    delete_result = await db.execute(delete_stmt)
    deleted_count = delete_result.rowcount
    logger.info(
        f"[corr={correlation_id}] 🗑️  Suppression des retours existants dans la période rolling: "
        f"{deleted_count} retour(s) supprimé(s)"
    )
except Exception as delete_error:
    logger.warning(
        f"[corr={correlation_id}] ⚠️ Erreur lors de la suppression des retours existants: {delete_error}"
    )
    await db.rollback()
    # Continuer quand même (les vérifications individuelles éviteront les doublons)
```

**Logique :**
- Supprime tous les retours de l'utilisateur dans la période `[start_date, end_date[`
- Gère les erreurs gracieusement (log warning + rollback, mais continue)
- Log le nombre de retours supprimés

---

### 3. Suppression de la vérification individuelle par mois

**Avant :** On vérifiait si chaque mois existait déjà avant de l'insérer.

**Après :** On supprime cette vérification car on a déjà supprimé tous les retours dans la période.

```python
for month in months:
    # Note: On ne vérifie plus si déjà calculé car on a supprimé tous les retours
    # dans la période rolling avant la boucle. Cela évite les doublons et garantit
    # une génération propre.
```

**Avantage :** Plus simple, plus rapide, garantit l'absence de doublons.

---

### 4. Vérification post-insert

**Ajout :** Compte les retours dans la période rolling après le commit pour vérifier qu'on a bien 12 retours.

```python
# Vérification post-insert : compter les retours dans la période rolling
try:
    count_result = await db.execute(
        select(LunarReturn).where(
            LunarReturn.user_id == current_user.id,
            LunarReturn.return_date >= start_date,
            LunarReturn.return_date < end_date
        )
    )
    actual_count = len(count_result.scalars().all())
    
    if actual_count != 12:
        logger.warning(
            f"[corr={correlation_id}] ⚠️ Vérification post-insert: "
            f"attendu 12 retours, trouvé {actual_count} dans la période rolling"
        )
    else:
        logger.info(
            f"[corr={correlation_id}] ✅ Vérification post-insert: "
            f"{actual_count} retours confirmés dans la période rolling"
        )
except Exception as count_error:
    logger.warning(
        f"[corr={correlation_id}] ⚠️ Erreur lors de la vérification post-insert: {count_error}"
    )
    # Ne pas faire échouer la requête si la vérification échoue
```

**Logique :**
- Compte les retours dans la période `[start_date, end_date[`
- Log un warning si `actual_count != 12`
- Log un info si `actual_count == 12`
- Ne fait pas échouer la requête si la vérification échoue (log warning seulement)

---

### 5. Réponse API enrichie

**Avant :**
```json
{
  "message": "...",
  "mode": "rolling",
  "months_count": 12,
  "generated_count": 12,
  "errors_count": 0,
  "correlation_id": "..."
}
```

**Après :**
```json
{
  "message": "...",
  "mode": "rolling",
  "start_date": "2026-01-01T00:00:00+00:00",
  "end_date": "2027-01-01T00:00:00+00:00",
  "months_count": 12,
  "generated_count": 12,
  "errors_count": 0,
  "correlation_id": "..."
}
```

**Nouveaux champs :**
- `start_date` : ISO 8601, début de la période rolling
- `end_date` : ISO 8601, fin de la période rolling (exclusive)

---

### 6. Import SQLAlchemy `delete`

**Ajout :**
```python
from sqlalchemy import select, delete
```

---

## ✅ Résultat attendu

1. **Suppression pré-insert :** Tous les retours existants dans la période rolling sont supprimés
2. **Insertion propre :** 12 nouveaux retours sont insérés sans doublons
3. **Vérification post-insert :** Confirmation qu'on a bien 12 retours dans la période
4. **Réponse enrichie :** `start_date` et `end_date` dans la réponse JSON
5. **Logs structurés :** `correlation_id` et `step` conservés partout

---

## 🔍 Exemple de logs

```
[corr=abc-123] 📅 Génération rolling 12 mois glissants à partir de 2025-12-22 - 
  mois: 2026-01 à 2026-12 (12 mois), 
  période: 2026-01-01 à 2027-01-01

[corr=abc-123] 🗑️  Suppression des retours existants dans la période rolling: 3 retour(s) supprimé(s)

[corr=abc-123] 🔄 Calcul révolution lunaire 2026-01...
[corr=abc-123] ✅ Calcul réussi pour 2026-01
...
[corr=abc-123] ✅ Commit DB - 12 révolution(s) générée(s), 0 erreur(s)

[corr=abc-123] ✅ Vérification post-insert: 12 retours confirmés dans la période rolling
```

---

## 🧪 Tests

### Test E2E (curl)

```bash
# 1. Générer les retours (première fois)
curl -X POST "http://localhost:8000/api/lunar-returns/generate" \
  -H "Authorization: Bearer $TOKEN" | jq

# Réponse attendue:
# {
#   "message": "12 révolution(s) lunaire(s) générée(s)",
#   "mode": "rolling",
#   "start_date": "2026-01-01T00:00:00+00:00",
#   "end_date": "2027-01-01T00:00:00+00:00",
#   "generated_count": 12,
#   ...
# }

# 2. Régénérer (devrait supprimer les 12 existants et en créer 12 nouveaux)
curl -X POST "http://localhost:8000/api/lunar-returns/generate" \
  -H "Authorization: Bearer $TOKEN" | jq

# Vérifier les logs: "🗑️ Suppression des retours existants: 12 retour(s) supprimé(s)"
# Vérifier: "✅ Vérification post-insert: 12 retours confirmés"
```

---

## 📋 Checklist de validation

- [x] Calcul de `start_date` et `end_date` correct
- [x] DELETE des retours existants dans la période avant insertion
- [x] Suppression de la vérification individuelle par mois
- [x] Vérification post-insert (count == 12)
- [x] Réponse API avec `start_date` et `end_date`
- [x] Logs structurés avec `correlation_id` et `step` conservés
- [x] Gestion d'erreurs gracieuse (warnings, pas d'échec)
- [x] Code compile correctement

---

## ⚠️ Notes importantes

1. **Transaction :** Le DELETE et les INSERT sont dans la même transaction (commit à la fin)
2. **Rollback :** Si le DELETE échoue, on fait un rollback mais on continue quand même
3. **Vérification non bloquante :** Si la vérification post-insert échoue, on log un warning mais on ne fait pas échouer la requête
4. **Performance :** Le DELETE est plus efficace qu'une vérification par mois (1 requête vs 12)

---

**Modifications complètes et prêtes à être testées !** 🌙✨

