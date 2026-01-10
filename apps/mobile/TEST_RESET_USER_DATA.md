# Test Manuel : Reset User Data (Local) + Anti-Flash + Migration One-Shot

## Objectif

Vérifier que le reset complet des données locales fonctionne de manière atomique et que le routing ne rebondit pas.
Vérifier qu'il n'y a AUCUN flash du Home avant redirection.
Vérifier que la migration ghost-flags ne s'exécute qu'une seule fois.

## Prérequis

- App en mode DEV (`__DEV__ === true`)
- Au moins quelques données créées :
  - Onboarding complété
  - Au moins 1 entrée de journal
  - Notifications activées (optionnel)

## Étapes de Test

### 1. Préparer l'état initial

1. Lancer l'app
2. Compléter l'onboarding (welcome → consent → profile → disclaimer → onboarding)
3. Créer au moins 1 entrée de journal
4. Aller dans Réglages
5. Vérifier que vous êtes sur l'écran Home (pas de redirection)

### 2. Tester le Reset depuis Settings

1. Dans Réglages, scroller jusqu'à la section "Actions"
2. Cliquer sur "🗑️ Supprimer mes données locales"
3. **Vérifier l'Alert de confirmation** :
   - Liste des données qui seront supprimées
   - Bouton "Annuler" et "Supprimer"
4. Cliquer sur "Supprimer"
5. **Observer les logs dans la console** (ordre attendu) :
   ```
   [Settings] 🗑️ Début reset des données locales...
   [ResetService] 🗑️ START: Reset complet des données locales
   [ResetService] Step 1: Annulation des notifications...
   [ResetService] ✅ Notifications annulées
   [ResetService] Step 2: Suppression des entrées de journal...
   [ResetService] ✅ Journal supprimé (X entrées)
   [ResetService] Step 3: Suppression du cache lunaire...
   [ResetService] ✅ Cache lunaire supprimé
   [ResetService] Step 4: Reset du store onboarding...
   [ResetService] ✅ Store onboarding reset
   [ResetService] Step 5: Clear du store cycle...
   [ResetService] ✅ Store cycle cleared
   [ResetService] Step 6: Clear du store natal...
   [ResetService] ✅ Store natal cleared
   [ResetService] Step 7: Logout (suppression token auth)...
   [ResetService] ✅ Auth cleared (token supprimé)
   [ResetService] Step 8: Suppression des données de profil...
   [ResetService] ✅ Données de profil supprimées (X clés)
   [ResetService] Step 9: Suppression des clés menstrual_* et onboarding_step...
   [ResetService] ✅ Clés menstrual_* et onboarding_step supprimées (X clés)
   [ResetService] ✅ END: Reset complet terminé avec succès
   [Settings] ✅ Reset terminé, navigation vers /welcome...
   [Settings] ✅ Flag isResetting relâché
   ```
6. **Vérifier la navigation** :
   - Redirection automatique vers `/welcome`
   - Pas de rebond vers d'autres écrans
   - Pas de log `[INDEX] ⏸️ Reset en cours, skip routing` après la navigation

### 3. Vérifier l'état après Reset

1. Sur l'écran Welcome, vérifier que :
   - L'écran s'affiche correctement
   - Pas de redirection automatique vers Home
2. Compléter l'onboarding étape par étape :
   - Welcome → Consent → Profile → Disclaimer → Onboarding (slides)
   - **Vérifier qu'il n'y a PAS de rebond** (pas de retour en arrière)
   - Chaque étape doit progresser normalement (1→2→3→slides)
3. Sur les slides onboarding :
   - **Test A : "Passer" (skip)** :
     - Cliquer sur "Passer"
     - **Vérifier les logs** : `[OnboardingStore] ✅ completeOnboarding()`
     - **Vérifier la navigation** : Redirection directe vers `/` (Home), **AUCUN rebond**
   - **Test B : "Commencer" (après dernier slide)** :
     - Cliquer sur "Suivant" jusqu'au dernier slide
     - Cliquer sur "Commencer"
     - **Vérifier la navigation** : Redirection directe vers `/` (Home), **AUCUN rebond**
4. Après onboarding complet :
   - Redirection vers Home
   - Journal vide (pas d'anciennes entrées)
   - Notifications désactivées

### 4. Tests Anti-Flash + Double-Run + Migration One-Shot

#### Test 4.1 : Anti-Flash Home

**Objectif :** Vérifier qu'il n'y a AUCUN flash du Home avant redirection vers onboarding/login

1. **Fresh install** (ou reset complet)
2. Lancer l'app
3. **Observer visuellement** :
   - ✅ AUCUN flash de l'écran Home ne doit être visible
   - ✅ Redirection immédiate vers `/welcome` (sans affichage intermédiaire du Home)
4. **Vérifier les logs** :
   - ✅ PAS de log `[INDEX] ✅ Tous les guards passés → Home` avant redirection
   - ✅ Log attendu : `[INDEX] → Redirection /welcome`

#### Test 4.2 : Double-Run Protection

**Objectif :** Vérifier que le guard de routing ne s'exécute pas en double

1. Fresh install
2. Lancer l'app
3. **Vérifier les logs** :
   - ✅ Le log `[INDEX] 📍 Début checkRouting` ne doit apparaître qu'UNE seule fois
   - ✅ Si un second run est tenté, voir : `[INDEX] ⏸️ Routing déjà en cours, skip double-run`
4. Compléter l'onboarding
5. Arrivée sur Home
6. **Vérifier les logs** :
   - ✅ PAS de spam de logs de routing après l'arrivée sur Home

#### Test 4.3 : Migration One-Shot

**Objectif :** Vérifier que la migration ghost-flags ne s'exécute qu'une seule fois

1. **Fresh install** (ou reset complet)
2. Lancer l'app
3. **Vérifier les logs (première exécution)** :
   - ✅ Log attendu : `[Migration] 🔄 Première exécution : nettoyage des flags fantômes...`
   - ✅ Log attendu : `[Migration] ✅ Migration terminée, marquée comme effectuée`
4. Fermer l'app (force quit)
5. Relancer l'app
6. **Vérifier les logs (deuxième+ exécution)** :
   - ✅ AUCUN log `[Migration]` ne doit apparaître (migration déjà effectuée)
7. Relancer l'app plusieurs fois
8. **Vérifier** :
   - ✅ La migration ne log jamais à nouveau (vraiment one-shot)

#### Test 4.4 : Fresh install → Onboarding complet

1. **Fresh install** (ou reset complet)
2. Compléter l'onboarding :
   - Welcome → Consent → Profile → Disclaimer → Slides onboarding
3. Sur les slides, cliquer sur **"Commencer"** (après dernier slide)
4. **Vérifier** :
   - ✅ Navigation directe vers `/` (Home)
   - ✅ **AUCUN rebond** (pas de retour vers disclaimer ou autre)
   - ✅ Logs : `[OnboardingStore] ✅ completeOnboarding() - Terminé`
   - ✅ L'écran Home s'affiche correctement

#### Test 4.5 : Reset depuis Settings → Refaire onboarding → Aucun rebond

1. Aller dans **Réglages** → **"🗑️ Supprimer mes données locales"**
2. Confirmer la suppression
3. **Vérifier** : Redirection vers `/welcome`
4. Refaire l'onboarding complet :
   - Welcome → Consent → Profile → Disclaimer → Slides onboarding
5. Cliquer sur **"Passer"** (skip slides)
6. **Vérifier** :
   - ✅ Navigation directe vers `/` (Home)
   - ✅ **AUCUN rebond** (pas de retour en arrière)
   - ✅ Progression normale 1→2→3→slides→Home

### 5. Tester depuis DEV QA Tools (optionnel)

1. Aller dans Réglages → Section "🔧 DEV QA Tools"
2. Cliquer sur "🗑️ Reset User Data (Local)"
3. Vérifier le même comportement que depuis le bouton principal

## Critères de Succès

✅ **Reset atomique** : Toutes les données sont supprimées avant navigation
✅ **Pas de rebond routing** : Navigation directe vers `/welcome`, pas de rebond
✅ **Onboarding propre** : Progression 1→2→3→slides sans retour en arrière
✅ **Anti-flash Home** : AUCUN flash du Home ne doit être visible avant redirection
✅ **Double-run protection** : Le guard ne s'exécute pas en double (log `skip double-run` si tenté)
✅ **Migration one-shot** : La migration ghost-flags ne s'exécute qu'une seule fois (flag `MIGRATION_GHOSTFLAGS_DONE`)
✅ **Guard indépendant** : Le guard de routing ne dépend PAS de flags `menstrual_*`
✅ **Logs cohérents** : Ordre des logs respecté, pas d'erreur
✅ **Flag isResetting** : Bloque le routing pendant le reset, relâché après navigation

## LOGS ATTENDUS (FLOW COMPLET)

### Flow Normal : Fresh Install → Onboarding Complet → Home

```
[Migration] 🔄 Première exécution : nettoyage des flags fantômes...
[Migration] ✅ Migration terminée, marquée comme effectuée
[OnboardingStore] 💧 Hydratation depuis AsyncStorage...
[OnboardingStore] ✅ Hydraté: {hasSeenWelcomeScreen: false, hasCompletedProfile: false, ...}
[INDEX] 📍 Début checkRouting
[INDEX] → Redirection /welcome
[WELCOME] ✅ Composant Welcome monté et affiché à l'écran
[WELCOME] Bouton "Continuer" cliqué
[WELCOME] hasSeenWelcomeScreen défini à true via useOnboardingStore
[ONBOARDING_FLOW] from=WELCOME nextStep=/onboarding/consent state={welcome=true, consent=false, profile=false, disclaimer=false, completed=false}
[ONBOARDING_FLOW] from=CONSENT nextStep=/onboarding/profile-setup state={welcome=true, consent=true, profile=false, disclaimer=false, completed=false}
[PROFILE-SETUP] Géocodage du lieu: Paris, France
[PROFILE-SETUP] Coordonnées: {latitude: 48.8566, longitude: 2.3522}
[PROFILE-SETUP] ✅ Profil sauvegardé (hasCompletedProfile=true)
[PROFILE-SETUP] Calcul du thème natal...
[PROFILE-SETUP] ✅ Thème natal calculé automatiquement
[ONBOARDING_FLOW] from=PROFILE-SETUP nextStep=/onboarding/disclaimer state={welcome=true, consent=true, profile=true, disclaimer=false, completed=false}
[ONBOARDING_FLOW] from=DISCLAIMER nextStep=/onboarding state={welcome=true, consent=true, profile=true, disclaimer=true, completed=false}
[ONBOARDING] Slides montées, étape: 0
[ONBOARDING] Dernier slide → completeOnboarding()
[OnboardingStore] ✅ completeOnboarding() - Toutes les préconditions OK
[OnboardingStore] ✅ completeOnboarding() - Terminé
[ONBOARDING] ✅ completeOnboarding réussi, navigation vers /
[INDEX] 📍 Début checkRouting
[INDEX] ✅ Tous les guards passés → Home
```

### Flow Reset → Refaire Onboarding

```
[Settings] 🗑️ Début reset des données locales...
[ResetService] 🗑️ START: Reset complet des données locales
[ResetService] Step 1: Annulation des notifications...
[ResetService] ✅ Notifications annulées
[ResetService] Step 2: Suppression des entrées de journal...
[ResetService] ✅ Journal supprimé (X entrées)
[ResetService] Step 3: Suppression du cache lunaire...
[ResetService] ✅ Cache lunaire supprimé
[ResetService] Step 4: Reset du store onboarding...
[ResetService] ✅ Store onboarding reset
[ResetService] Step 5: Clear du store cycle...
[ResetService] ✅ Store cycle cleared
[ResetService] Step 6: Clear du store natal...
[ResetService] ✅ Store natal cleared
[ResetService] Step 7: Logout (suppression token auth)...
[ResetService] ✅ Auth cleared (token supprimé)
[ResetService] Step 8: Suppression des données de profil...
[ResetService] ✅ Données de profil supprimées (X clés)
[ResetService] Step 9: Suppression des clés menstrual_* et onboarding_step...
[ResetService] ✅ Clés menstrual_* et onboarding_step supprimées (X clés)
[ResetService] ✅ END: Reset complet terminé avec succès
[Settings] ✅ Reset terminé, navigation vers /welcome...
[Settings] ✅ Flag isResetting relâché
[WELCOME] ✅ Composant Welcome monté et affiché à l'écran
```

## SCÉNARIOS DE TEST PRIORITAIRES

### Scénario 1 : Fresh Install → Onboarding Complet (Commencer)
**Objectif :** Vérifier le flow complet sans aucune donnée préexistante

1. Fresh install (ou reset complet)
2. Lancer l'app
3. ✅ VÉRIFIER : Aucun flash Home, redirection immédiate vers `/welcome`
4. Cliquer sur "Commencer" (welcome)
5. ✅ VÉRIFIER : Log `[ONBOARDING_FLOW] from=WELCOME nextStep=/onboarding/consent`
6. Accepter le consentement
7. ✅ VÉRIFIER : Log `[ONBOARDING_FLOW] from=CONSENT nextStep=/onboarding/profile-setup`
8. Remplir le profil et valider
9. ✅ VÉRIFIER : Log `[PROFILE-SETUP] ✅ Profil sauvegardé (hasCompletedProfile=true)`
10. ✅ VÉRIFIER : Log `[ONBOARDING_FLOW] from=PROFILE-SETUP nextStep=/onboarding/disclaimer`
11. Accepter le disclaimer
12. ✅ VÉRIFIER : Log `[ONBOARDING_FLOW] from=DISCLAIMER nextStep=/onboarding`
13. Cliquer sur "Suivant" jusqu'au dernier slide, puis "Commencer"
14. ✅ VÉRIFIER : Log `[OnboardingStore] ✅ completeOnboarding() - Terminé`
15. ✅ VÉRIFIER : Navigation directe vers `/` (Home), AUCUN rebond
16. ✅ VÉRIFIER : Écran Home s'affiche correctement

### Scénario 2 : Fresh Install → Onboarding Skip (Passer)
**Objectif :** Vérifier que le skip fonctionne sans rebond

1. Fresh install (ou reset complet)
2. Compléter les étapes : welcome → consent → profile → disclaimer
3. Arriver sur les slides onboarding
4. Cliquer sur "Passer" (skip)
5. ✅ VÉRIFIER : Log `[OnboardingStore] ✅ completeOnboarding() - Terminé`
6. ✅ VÉRIFIER : Navigation directe vers `/` (Home), AUCUN rebond
7. ✅ VÉRIFIER : Écran Home s'affiche correctement

### Scénario 3 : Reset depuis Settings → Refaire Onboarding
**Objectif :** Vérifier que le reset atomique fonctionne et que le refaire l'onboarding ne rebondit pas

1. Avoir des données existantes (onboarding complété, journal non vide)
2. Aller dans Réglages → "🗑️ Supprimer mes données locales"
3. Confirmer la suppression
4. ✅ VÉRIFIER : Logs de reset complet (voir section "LOGS ATTENDUS")
5. ✅ VÉRIFIER : Redirection vers `/welcome`, pas de rebond
6. Refaire l'onboarding complet : welcome → consent → profile → disclaimer → slides
7. ✅ VÉRIFIER : Progression normale 1→2→3→slides, AUCUN retour en arrière
8. Cliquer sur "Passer" (ou "Commencer")
9. ✅ VÉRIFIER : Navigation directe vers `/` (Home), AUCUN rebond
10. ✅ VÉRIFIER : Journal vide, pas d'anciennes données

### Scénario 4 : Migration One-Shot
**Objectif :** Vérifier que la migration ghost-flags ne s'exécute qu'une seule fois

1. Fresh install (ou reset complet avec suppression de `MIGRATION_GHOSTFLAGS_DONE`)
2. Lancer l'app
3. ✅ VÉRIFIER : Log `[Migration] 🔄 Première exécution : nettoyage des flags fantômes...`
4. ✅ VÉRIFIER : Log `[Migration] ✅ Migration terminée, marquée comme effectuée`
5. Fermer l'app (force quit)
6. Relancer l'app
7. ✅ VÉRIFIER : AUCUN log `[Migration]` ne doit apparaître (déjà effectuée)
8. Relancer l'app 5+ fois
9. ✅ VÉRIFIER : La migration ne log jamais à nouveau (vraiment one-shot)

### Scénario 5 : Anti-Flash + Double-Run Protection
**Objectif :** Vérifier qu'il n'y a aucun flash Home et que le guard ne s'exécute pas en double

1. Fresh install (ou reset complet)
2. Lancer l'app
3. ✅ VÉRIFIER VISUELLEMENT : AUCUN flash de l'écran Home ne doit être visible
4. ✅ VÉRIFIER : Log `[INDEX] 📍 Début checkRouting` apparaît UNE seule fois
5. ✅ VÉRIFIER : Si un second run est tenté, voir : `[INDEX] ⏸️ Routing déjà en cours, skip double-run`
6. Compléter l'onboarding jusqu'à Home
7. ✅ VÉRIFIER : PAS de spam de logs de routing après l'arrivée sur Home
8. ✅ VÉRIFIER : `isCheckingRouting` reste à `true` pendant toutes les redirections (anti-flash)

## Problèmes Connus / Notes

- Le flag `isResetting` est relâché après 500ms de délai pour laisser la navigation se faire
- Si le reset échoue, le flag est immédiatement relâché pour éviter de bloquer l'app
- Les données serveur (si existantes) ne sont PAS supprimées, seulement les données locales
- **PATCH V2** : L'étape "Cycles menstruels" (4/4) a été SUPPRIMÉE du flow onboarding
- Le cycle menstruel est désormais une feature post-onboarding accessible via Settings/Profil
- La migration ghost-flags utilise `MIGRATION_GHOSTFLAGS_DONE` pour ne s'exécuter qu'une fois
- Le guard de routing utilise `routingInFlightRef` pour éviter les doubles exécutions
- `isCheckingRouting` reste à `true` pendant les redirections (anti-flash Home)
- **PATCH V3** : Navigation centralisée via `services/onboardingFlow.ts` (fonction pure + helper avec logs)

