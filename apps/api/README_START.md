# 🚀 Guide de Démarrage de l'API

## ⚠️ IMPORTANT : Accès depuis Device Mobile

Pour que l'app mobile Expo puisse accéder à l'API depuis un device physique, l'API **DOIT** être démarrée avec `--host 0.0.0.0`.

## ✅ Méthode Recommandée

### Option 1 : Utiliser le script start_api.sh (RECOMMANDÉ)

```bash
cd apps/api
./start_api.sh
```

Ce script démarre automatiquement avec `--host 0.0.0.0`.

### Option 2 : Commande manuelle

```bash
cd apps/api
source .venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Option 3 : Python main.py

```bash
cd apps/api
source .venv/bin/activate
python main.py
```

Cette méthode utilise `settings.API_HOST` depuis `.env` (par défaut `0.0.0.0`).

## ❌ NE PAS FAIRE

```bash
# ❌ Cette commande écoute seulement sur 127.0.0.1 (localhost)
uvicorn main:app --reload

# ❌ Cette commande aussi
uvicorn main:app --reload --port 8000
```

## 🔍 Vérification

Après démarrage, vérifiez que l'API écoute sur toutes les interfaces :

```bash
# Doit afficher 0.0.0.0.8000 (pas seulement 127.0.0.1.8000)
netstat -an | grep 8000
```

Test depuis le Mac :

```bash
# Doit fonctionner
curl http://127.0.0.1:8000/health

# Doit aussi fonctionner (remplacez par votre IP LAN)
curl http://192.168.0.150:8000/health
```

Si le deuxième test échoue mais pas le premier, l'API n'écoute pas sur `0.0.0.0`.

## 📱 Configuration Mobile

Dans `apps/mobile/.env`, définissez :

```env
EXPO_PUBLIC_API_URL=http://192.168.0.150:8000
```

(Remplacez `192.168.0.150` par l'IP de votre Mac sur le réseau local)

Pour trouver votre IP LAN :

```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

