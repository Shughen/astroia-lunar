# 🔧 Instructions pour relancer l'API correctement

## ❌ Problème actuel
L'API tourne actuellement avec :
```bash
uvicorn main:app --reload --port 8000
```
→ Elle écoute **uniquement sur localhost (127.0.0.1)**, pas sur l'IP LAN (192.168.0.150)

## ✅ Solution

### Étape 1 : Arrêter l'API actuelle
Dans le terminal où l'API tourne (PID 98122), appuyez sur **Ctrl+C**

### Étape 2 : Relancer avec le bon host

**Option A : Utiliser le script (recommandé)**
```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api
./start_api.sh
```

**Option B : Lancer manuellement**
```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api
source .venv/bin/activate  # Si vous utilisez un venv
uvicorn main:app --reload --port 8000 --host 0.0.0.0
```

### Étape 3 : Vérification

Une fois relancée, testez :
```bash
# Depuis votre Mac
curl http://192.168.0.150:8000/health

# Vous devriez voir :
# {"status":"healthy","checks":{...}}
```

## 🔍 Vérification que ça fonctionne

L'API doit écouter sur `0.0.0.0:8000` :
```bash
netstat -an | grep 8000 | grep LISTEN
# Devrait afficher : tcp4 ... 0.0.0.0.8000 ... LISTEN
# (pas seulement 127.0.0.1.8000)
```

## ⚠️ Firewall macOS

Si ça ne fonctionne toujours pas après avoir relancé, vérifiez le pare-feu :
- **Préférences Système** → **Sécurité** → **Pare-feu**
- Autoriser les connexions entrantes pour Python/uvicorn

