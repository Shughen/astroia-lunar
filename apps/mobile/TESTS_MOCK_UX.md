# Tests Manuels - Amélioration UX Mode Mock

## Contexte
Amélioration de l'affichage en mode mock (DEV_MOCK_RAPIDAPI=true) pour les 3 fonctionnalités Luna Pack :
- Lunar Mansion
- Void of Course  
- Lunar Return Report

## Prérequis
1. Backend configuré avec `DEV_MOCK_RAPIDAPI=true`
2. Application mobile lancée en mode développement
3. Accès à l'écran Luna Pack (`/lunar/index`)

## Checklist de Tests

### 1. Lunar Mansion

**Actions :**
1. Aller sur l'écran Luna Pack
2. Cliquer sur le bouton "🏰 Lunar Mansion"
3. Attendre le chargement de la réponse

**Vérifications attendues :**
- [ ] Un badge violet/neutre "MOCK" apparaît à côté du titre "🏰 Lunar Mansion"
- [ ] Le texte "Provider: mock (dev)" est affiché (au lieu de "Provider: rapidapi")
- [ ] Le résumé affiche toujours "💬 Données de démonstration (mode dev)." (même si interpretation est absent dans le JSON)
- [ ] Le JSON brut (via bouton "Voir JSON complet") contient toujours `_mock: true` et `_reason`

**Résultat attendu :**
```
🏰 Lunar Mansion          [MOCK]
Provider: mock (dev)

Résumé
🏰 Mansion #X: Nom de la mansion
💬 Données de démonstration (mode dev).
```

---

### 2. Void of Course

**Actions :**
1. Sur l'écran Luna Pack
2. Cliquer sur le bouton "🌑 Void of Course"
3. Attendre le chargement de la réponse

**Vérifications attendues :**
- [ ] Un badge violet/neutre "MOCK" apparaît à côté du titre "🌑 Void of Course"
- [ ] Le texte "Provider: mock (dev)" est affiché
- [ ] Les données VoC sont affichées normalement (is_void, fenêtres, etc.)
- [ ] Le JSON brut contient toujours `_mock: true` et `_reason`

**Résultat attendu :**
```
🌑 Void of Course         [MOCK]
Provider: mock (dev)

Résumé
✅ Actif (ou ❌ Inactif)
🕐 Début: [date/heure]
🕐 Fin: [date/heure]
🌙 Signe lunaire: [signe]
```

---

### 3. Lunar Return Report

**Actions :**
1. Sur l'écran Luna Pack
2. Cliquer sur le bouton "🌙 Lunar Return Report"
3. Attendre le chargement de la réponse

**Vérifications attendues :**
- [ ] Un badge violet/neutre "MOCK" apparaît à côté du titre "🌙 Lunar Return Report"
- [ ] Le texte "Provider: mock (dev)" est affiché
- [ ] Le résumé affiche toujours "💬 Données de démonstration (mode dev)." (même si interpretation est absent dans le JSON)
- [ ] Les autres données (date de retour, lune, maison) sont affichées normalement
- [ ] Le JSON brut contient toujours `_mock: true` et `_reason`

**Résultat attendu :**
```
🌙 Lunar Return Report    [MOCK]
Provider: mock (dev)

Résumé
📅 Date de retour: [date]
🌙 Lune: [signe] ([degré]°)
🏠 Maison: [numéro]
💬 Données de démonstration (mode dev).
```

---

## Tests de Non-Régression

### Mode Production (sans mock)

**Actions :**
1. Désactiver `DEV_MOCK_RAPIDAPI` côté backend (ou utiliser un environnement de production)
2. Tester les 3 fonctionnalités

**Vérifications attendues :**
- [ ] Pas de badge "MOCK" visible
- [ ] Le texte "Provider: rapidapi" est affiché
- [ ] Les interprétations normales sont affichées (pas de texte "Données de démonstration")
- [ ] Les données sont réelles (pas mock)

---

## Notes

- Le JSON brut reste accessible via le bouton "Voir JSON complet" pour le debug
- Les changements sont uniquement côté UI, le contrat backend reste inchangé
- Le helper `isMockResponse()` détecte `data._mock` ou `_mock` à la racine
- **En mode mock** : la ligne 💬 est toujours affichée avec "Données de démonstration (mode dev)." même si `interpretation` est absent dans le JSON
- **En mode production** : la ligne 💬 n'est affichée que si `interpretation` existe dans les données
- Le badge MOCK utilise un style violet/neutre (moins "warning") pour s'harmoniser avec le thème de l'app

