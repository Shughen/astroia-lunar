#!/bin/bash

# Script de smoke tests pour Astroia Lunar API

API_URL="http://localhost:8000"
PASS=0
FAIL=0

echo "🧪 Astroia Lunar - Smoke Tests"
echo "=============================="
echo ""

# Test 1: Health
echo -n "1. Health Check... "
if curl -s "$API_URL/health" | grep -q "healthy"; then
  echo "✅"
  ((PASS++))
else
  echo "❌"
  ((FAIL++))
fi

# Test 2: Root
echo -n "2. Root Status... "
if curl -s "$API_URL/" | grep -q "running"; then
  echo "✅"
  ((PASS++))
else
  echo "❌"
  ((FAIL++))
fi

# Test 3: Mansion
echo -n "3. Lunar Mansion... "
RESPONSE=$(curl -s --max-time 10 -X POST "$API_URL/api/lunar/mansion" \
  -H "Content-Type: application/json" \
  -d '{"datetime_location":{"year":2025,"month":11,"day":11,"hour":12,"minute":0,"second":0,"city":"Paris","country_code":"FR"},"system":"arabian_tropical","days_ahead":28}')
  
if echo "$RESPONSE" | grep -q "lunar_mansion"; then
  echo "✅"
  ((PASS++))
else
  echo "❌"
  ((FAIL++))
fi

# Test 4: VoC Current
echo -n "4. VoC Current... "
if curl -s "$API_URL/api/lunar/voc/current" | grep -q "is_active\|message"; then
  echo "✅"
  ((PASS++))
else
  echo "❌"
  ((FAIL++))
fi

# Test 5: Mansion Today
echo -n "5. Mansion Today... "
if curl -s "$API_URL/api/lunar/mansion/today" | grep -q "date\|message"; then
  echo "✅"
  ((PASS++))
else
  echo "❌"
  ((FAIL++))
fi

echo ""
echo "=============================="
echo "📊 Résultat: $PASS/5 tests passés"
echo ""

if [ $FAIL -eq 0 ]; then
  echo "🎉 Tous les smoke tests ont réussi !"
  exit 0
else
  echo "⚠️  $FAIL tests ont échoué"
  exit 1
fi
