# 🧪 Astroia Lunar - Smoke Tests QA

Tests rapides pour valider que l'API fonctionne correctement.

---

## ⚡ Quick Smoke Tests (10 commandes)

Voir le script automatisé dans `scripts/smoke-test.sh`

**Lancer tous les tests** :
```bash
make smoke
```

Ou directement :
```bash
bash scripts/smoke-test.sh
```

---

## 📋 Tests Inclus

1. **Health Check** - `/health`
2. **Root Status** - `/`
3. **Lunar Mansion** - `/api/lunar/mansion` (POST)
4. **VoC Current** - `/api/lunar/voc/current`
5. **Mansion Today** - `/api/lunar/mansion/today`
6. **Calendar Month** - `/api/calendar/month`
7. **Natal Chart** - `/api/natal-chart/external` (POST)
8. **VoC Next Window** - `/api/lunar/voc/next_window`
9. **OpenAPI Schema** - `/openapi.json`
10. **Swagger Docs** - `/docs`

---

## ✅ Résultat Attendu

```
🧪 Astroia Lunar - Smoke Tests
==============================

1. Health Check... ✅
2. Root Status... ✅
3. Lunar Mansion... ✅
4. VoC Current... ✅
5. Mansion Today... ✅
6. Calendar Month... ✅
7. Natal Chart... ✅
8. VoC Next Window... ✅
9. OpenAPI Schema... ✅
10. Swagger Docs... ✅

==============================
📊 Résultat: 10/10 tests passés

🎉 Tous les smoke tests ont réussi !
```

---

## 🔧 Troubleshooting

### "API non accessible"
➡️ Lancez l'API : `make api` ou `astroia-start`

### "Tests échouent"
➡️ Vérifiez le health check : `curl http://localhost:8000/health`

### "Timeout sur endpoints RapidAPI"
➡️ Normal, le timeout est de 10s. Réessayez.

---

**Durée totale des smoke tests : < 30 secondes** ⚡
