# Checklist de Tests UX v3.0 - Corrections P0/P1

**Date** : 30 janvier 2026
**Commits** : df7a632, 43b1fac, 6daed3d
**Objectif** : Vérifier toutes les corrections UX avant publication bêta

---

## 🔧 Préparation

### 1. Compilation et Démarrage
```bash
cd apps/mobile
npx tsc --noEmit  # Doit être 0 erreur ✅
npm start         # Démarrer Expo
```

### 2. Lancer sur Android Studio
- Ouvrir Android Studio
- Sélectionner l'émulateur ou appareil physique
- Presser `a` dans le terminal Expo pour ouvrir sur Android

---

## ✅ Tests P0 (Critiques)

### P0-1 : Tutoiement Harmonisé

#### Journal (`/journal`)
- [ ] **Placeholder** : "Comment te sens-tu aujourd'hui ?" (ligne 281)
- [ ] **Sous-titre** : "Un espace pour ton rituel quotidien" (ligne 262)
- [ ] **Modal succès** : "Ton entrée a été enregistrée avec succès" (ligne 149)
- [ ] **Validation** : "Merci d'écrire quelque chose avant de sauvegarder" (ligne 120)
- [ ] **Erreur chargement** : "Impossible de charger tes entrées. Vérifie ta connexion." (ligne 107)
- [ ] **Erreur sauvegarde** : "Impossible de sauvegarder ton entrée. Vérifie ta connexion." (ligne 169)
- [ ] **Confirmation suppression** : "Veux-tu vraiment supprimer cette entrée ?" (ligne 180)
- [ ] **Empty state** : "Écris ta première entrée pour commencer !" (ligne 317)

**Comment tester** :
1. Ouvrir l'onglet Journal
2. Observer le placeholder du champ de saisie
3. Écrire une entrée et sauvegarder
4. Observer la modal de confirmation
5. Tester la suppression d'une entrée

---

#### Profil (`/(tabs)/profile`)
- [ ] **Footer version** : "Lunation v3.0" (ligne 400)
- [ ] **Footer description** : "Ton rituel lunaire quotidien" (ligne 401)
- [ ] **Permission notif** : "Merci d'autoriser les notifications dans les paramètres de ton appareil." (ligne 155)
- [ ] **Erreur générique** : "Merci de réessayer." (ligne 173)
- [ ] **Déconnexion** : "Es-tu sûr de vouloir te déconnecter ?" (ligne 181)

**Comment tester** :
1. Ouvrir l'onglet Profil
2. Scroller en bas pour voir la version
3. Tester le toggle notifications (si permission refusée)
4. Tester le bouton Déconnexion

---

#### Bottom Sheet "Aujourd'hui" (`components/TodayBottomSheet.tsx`)
- [ ] **Rituels Nouvelle Lune** :
  - "Renouvelle l'énergie de ton espace" (ligne 54)
- [ ] **Rituels Premier Croissant** :
  - "Une action concrète vers ton objectif" (ligne 57)
  - "Organise ta semaine" (ligne 59)
- [ ] **Rituels Lune Gibbeuse Décroissante** :
  - "Transmets ce que tu as appris" (ligne 77)
- [ ] **Rituels Dernier Quartier** :
  - "Pardonne-toi ou quelqu'un" (ligne 84)
- [ ] **Rituels Dernier Croissant** :
  - "Accorde-toi du temps" (ligne 87)

**Comment tester** :
1. Depuis Home, cliquer sur le bouton "Aujourd'hui"
2. Observer la section "Rituels suggérés"
3. Vérifier que tous les textes sont au tutoiement

---

#### Onboarding (`/onboarding/profile-setup`)
- [ ] **Validation nom** : "Merci d'entrer ton prénom" (ligne 182)
- [ ] **Validation lieu** : "Merci d'entrer ton lieu de naissance" (ligne 187)
- [ ] **Validation ville** : "Merci de choisir une ville dans la liste de suggestions" (ligne 195)
- [ ] **Validation heure** : "Merci d'entrer ton heure de naissance" (ligne 201)

**Comment tester** :
1. Se déconnecter
2. Créer un nouveau compte
3. Essayer de passer l'étape 2/4 sans remplir les champs
4. Vérifier les messages d'erreur

---

#### Backend Daily Climate (`apps/api/services/daily_climate.py`)
- [ ] **81 occurrences** de "vous/votre" remplacées par "tu/ton/ta"
- [ ] **0 occurrence** restante de vouvoiement

**Comment tester** :
1. Depuis Home, observer le message du jour dans le bottom sheet
2. Vérifier qu'il est au tutoiement
3. Tester plusieurs dates/phases lunaires si possible

---

### P0-2 : Version Affichée

- [ ] **Profil footer** : Affiche "Lunation v3.0" (pas v2.0)

**Comment tester** :
1. Onglet Profil
2. Scroller jusqu'en bas
3. Vérifier la version affichée

---

### P0-3 : Messages User-Friendly

- [ ] **Aucun message technique** visible ("Calcul API...", "Lieu requis")
- [ ] **Tous les "Veuillez"** remplacés par "Merci de"

**Comment tester** :
1. Parcourir tous les écrans
2. Tester les validations de formulaires
3. Vérifier qu'aucun message technique n'apparaît

---

## ✅ Tests P1 (Importants)

### P1-1 : Traduction Aspects Astrologiques

#### Thème Natal (`/natal-chart`)
- [ ] **Aspects majeurs** affichés en français :
  - Conjonction (☌)
  - Opposition (☍)
  - Carré (□)
  - Trigone (△)
  - Sextile (⚹)
- [ ] **Aucun terme anglais** (conjunction, square, etc.)

**Comment tester** :
1. Aller dans Thème Natal
2. Scroller jusqu'à "Aspects Majeurs"
3. Cliquer sur un aspect pour voir les détails
4. Vérifier que le nom de l'aspect est en français dans AspectDetailSheet

---

#### Révolution Lunaire (`/lunar-returns`)
- [ ] **Aspects du rapport** en français
- [ ] **Pas de termes anglais**

**Comment tester** :
1. Ouvrir la révolution lunaire du mois en cours
2. Observer les aspects listés
3. Vérifier qu'ils sont traduits

---

### P1-4 : Section Transits Vides

- [ ] **Widget Transits masqué** si aucun transit disponible
- [ ] **Pas de message** "Aucun transit majeur ce mois-ci"

**Comment tester** :
1. Depuis Home, observer si le widget "⭐ Transits Majeurs" est présent
2. Si absent : c'est normal, il n'y a pas de transits → ✅
3. Si présent : vérifier qu'il affiche bien des aspects

---

## 📊 Résultat Attendu

### Score UX
- **Avant** : 16.75/20
- **Après** : 18.5+/20 🎯

### Critères de Validation
- ✅ Tutoiement uniforme sur 100% des écrans
- ✅ Version v3.0 affichée correctement
- ✅ Aucun message technique visible
- ✅ Aspects en français partout
- ✅ Interface propre (pas de sections vides)

---

## 🐛 Bugs à Reporter

Si tu trouves un problème, note :
- **Écran** : Où se trouve le bug
- **Action** : Ce que tu as fait
- **Attendu** : Ce qui devrait se passer
- **Obtenu** : Ce qui se passe réellement
- **Screenshot** : Si possible

Format :
```
[ÉCRAN] Nom de l'écran
ACTION: Description de l'action
ATTENDU: Comportement attendu
OBTENU: Comportement observé
```

---

## ✅ Validation Finale

Une fois tous les tests passés :
- [ ] Compilation TypeScript sans erreur
- [ ] App démarre sans crash
- [ ] Tous les écrans testés
- [ ] Tous les textes en tutoiement
- [ ] Version v3.0 affichée
- [ ] Aspects en français

**Si tous les tests passent** → Prêt pour publication bêta ! 🚀
