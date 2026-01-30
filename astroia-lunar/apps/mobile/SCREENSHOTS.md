# Screenshots Lunation

## Capture Automatique ✅

### Commande Simple

```bash
npm run screenshots
```

**Résultat** : 8 screenshots dans `screenshots/`

### Ce qui est capturé

1. `12-home.png` - Dashboard "Mon Cycle"
2. `13-calendar.png` - Calendrier mensuel
3. `14-profile.png` - Profil utilisateur
4. `15-lunar-report-top.png` - Rapport lunaire (haut)
5. `16-lunar-report-bottom.png` - Rapport lunaire (bas)
6. `23-bottom-sheet-top.png` - Bottom sheet Aujourd'hui (haut)
7. `24-bottom-sheet-bottom.png` - Bottom sheet Aujourd'hui (bas)
8. `26-final-home.png` - Home final

### Prérequis

1. **Backend API** : `cd ../api && make run`
2. **Émulateur Android** : Pixel 7, API 34 lancé
3. **App installée** : `npx expo run:android`

### Durée

~2 minutes (navigation automatique avec Maestro)

### Flow Utilisé

`maestro/flows/capture-all-screens.yaml`

Navigation par coordonnées :
- Tabs : 17%, 50%, 83% (X) × 95% (Y)
- Hero card : 50%,35%
- TodayMiniCard : 50%,75%

## Ouvrir les Screenshots

```bash
open screenshots/
```

## Notes

- ✅ Fonctionne à 100%
- ✅ Pas de dépendances complexes
- ✅ Reproductible
- ⚠️ Onboarding non capturé (nécessite capture manuelle si besoin)

---

**Prêt pour Google Play Store** 🚀
