#!/bin/bash
# Script helper pour obtenir l'IP LAN du Mac
# Usage: ./scripts/print_lan_ip.sh

echo "🔍 Recherche de l'IP LAN..."

# Essayer en0 (Ethernet/WiFi principal sur macOS)
IP=$(ipconfig getifaddr en0 2>/dev/null)

if [ -z "$IP" ]; then
  # Fallback: chercher la première IP qui n'est pas localhost
  IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -1)
fi

if [ -z "$IP" ]; then
  echo "❌ Impossible de trouver l'IP LAN"
  echo "💡 Vérifiez que votre Mac est connecté au réseau Wi-Fi/Ethernet"
  exit 1
fi

echo ""
echo "✅ IP LAN trouvée: $IP"
echo ""
echo "📝 Ajoutez dans votre .env :"
echo "EXPO_PUBLIC_API_URL=http://$IP:8000"
echo ""
echo "🔧 Vérifiez que le backend écoute sur toutes les interfaces :"
echo "uvicorn main:app --host 0.0.0.0 --port 8000"

