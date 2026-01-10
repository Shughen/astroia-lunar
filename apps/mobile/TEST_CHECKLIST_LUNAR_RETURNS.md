# Checklist de test manuel - Lunar Returns MVP

## Prérequis

1. ✅ API backend lancée sur `http://localhost:8000` (ou `EXPO_PUBLIC_API_URL`)
2. ✅ App mobile lancée via `npx expo start`
3. ✅ Utilisateur connecté avec un token JWT valide

---

## Test 1: User sans retours → Empty state → Generate → Home affiche next

### Étapes

1. **Se connecter** avec un utilisateur qui n'a pas encore généré de retours lunaires
   - Email: `test@example.com`
   - Password: `password123`

2. **Vérifier l'écran Home**
   - ✅ Affiche le bloc "Prochain retour lunaire"
   - ✅ Affiche "Aucun retour lunaire généré pour le moment"
   - ✅ Affiche le bouton "Générer mes retours"

3. **Cliquer sur "Générer mes retours"**
   - ✅ Le bouton affiche un loader pendant la génération
   - ✅ Une alerte de succès apparaît: "Retours lunaires générés avec succès ! ✨"
   - ✅ Le bloc se met à jour automatiquement

4. **Vérifier le bloc mis à jour**
   - ✅ Affiche la date/heure du prochain retour lunaire (format: "15 janvier 2025, 14:30")
   - ✅ Affiche "dans X jours" (calcule correctement la différence)
   - ✅ Affiche "Lune en [signe]" si disponible
   - ✅ Affiche "Ascendant [signe]" si disponible
   - ✅ Affiche le bouton "Voir timeline"

---

## Test 2: Timeline affiche 12 items

### Étapes

1. **Sur l'écran Home, cliquer sur "Voir timeline"**

2. **Vérifier l'écran Timeline**
   - ✅ Affiche le titre "Timeline révolutions lunaires"
   - ✅ Affiche un bouton "← Retour" pour revenir en arrière
   - ✅ Affiche une liste de retours lunaires

3. **Vérifier les items de la liste**
   - ✅ Les items sont triés par `return_date` (ordre ascendant)
   - ✅ Chaque item affiche:
     - Date/heure formatée
     - Badge: "PASSÉ" (gris), "AUJOURD'HUI" (violet), "À VENIR" (vert)
     - Signe lunaire si disponible
     - Maison lunaire si disponible
     - Ascendant si disponible

4. **Vérifier le badge selon la date**
   - ✅ Dates passées: badge "PASSÉ" (gris)
   - ✅ Date du jour: badge "AUJOURD'HUI" (violet accent)
   - ✅ Dates futures: badge "À VENIR" (vert)

5. **Taper sur un item**
   - ✅ Ouvre un modal avec le JSON complet du retour lunaire
   - ✅ Le modal contient un bouton "Fermer"

6. **Vérifier le nombre d'items**
   - ✅ Affiche exactement 12 items (les 12 révolutions lunaires de l'année)

---

## Test 3: Offline → Error toast

### Étapes

1. **Désactiver la connexion réseau** (mode avion ou désactiver WiFi/data)

2. **Sur l'écran Home, cliquer sur "Générer mes retours"**
   - ✅ Affiche une alerte d'erreur
   - ✅ Le message indique une erreur réseau

3. **Sur l'écran Timeline, pull-to-refresh ou recharger**
   - ✅ Affiche une alerte d'erreur
   - ✅ Le message indique une erreur réseau

4. **Vérifier le format d'erreur structuré** (si backend renvoie `{detail, step, correlation_id}`)
   - ✅ Le message principal est affiché
   - ✅ Le `correlation_id` est affiché comme "Ref: [id]"
   - ✅ L'utilisateur peut copier le correlation_id

---

## Test 4: Erreurs API structurées

### Étapes

1. **Tester avec un utilisateur sans natal_chart**
   - Se connecter avec un utilisateur qui n'a pas de thème natal calculé
   - Cliquer sur "Générer mes retours"

2. **Vérifier l'erreur**
   - ✅ Affiche une alerte avec le message d'erreur du backend
   - ✅ Le format est: `{detail: "...", step: "fetch_natal_chart", correlation_id: "..."}`
   - ✅ Le message principal est clair: "Thème natal manquant. Calculez-le d'abord via POST /api/natal-chart"
   - ✅ Le `correlation_id` est affiché comme "Ref: [id]"

---

## Test 5: Navigation et UX

### Étapes

1. **Navigation Home → Timeline**
   - ✅ Le bouton "Voir timeline" sur Home navigue vers `/lunar-returns/timeline`
   - ✅ L'écran Timeline s'affiche correctement

2. **Navigation Timeline → Home**
   - ✅ Le bouton "← Retour" sur Timeline revient à l'écran précédent
   - ✅ Les données sont toujours chargées (pas de rechargement inutile)

3. **Loading states**
   - ✅ Home affiche un loader pendant le chargement du prochain retour
   - ✅ Timeline affiche un loader pendant le chargement de la liste
   - ✅ Le bouton "Générer" affiche un loader pendant la génération

---

## Résultats attendus

### ✅ Succès
- Tous les tests passent
- Aucune erreur console
- UX fluide et intuitive

### ❌ Échecs possibles
- Erreur réseau non gérée → Vérifier la gestion d'erreur
- Timeline vide alors qu'il y a des données → Vérifier l'appel API `getYear`
- Badge incorrect → Vérifier la logique de calcul des jours
- Date mal formatée → Vérifier `formatDate` et le fuseau horaire

---

## Notes

- Les erreurs TypeScript lors de la compilation ne sont pas bloquantes (Expo gère la compilation différemment)
- Vérifier que `EXPO_PUBLIC_API_URL` est bien configuré dans `.env`
- Vérifier que le token JWT est bien stocké dans `AsyncStorage` sous la clé `auth_token`

