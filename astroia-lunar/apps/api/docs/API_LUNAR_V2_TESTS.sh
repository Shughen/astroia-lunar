#!/bin/bash
# API Lunar V2 - Tests cURL
# Usage: ./API_LUNAR_V2_TESTS.sh

set -e

# Configuration
API_URL="${API_URL:-http://localhost:8000}"
TEST_EMAIL="${TEST_EMAIL:-test@example.com}"
TEST_PASSWORD="${TEST_PASSWORD:-test123}"

echo "🧪 Tests API Lunar V2"
echo "====================="
echo "API URL: $API_URL"
echo ""

# Couleurs
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# === 1. Health check ===
echo -e "${YELLOW}[1/5] Health check...${NC}"
HEALTH_RESPONSE=$(curl -s -w "\n%{http_code}" "$API_URL/health" || echo "000")
HTTP_CODE=$(echo "$HEALTH_RESPONSE" | tail -n1)

if [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ API is running${NC}"
else
    echo -e "${RED}❌ API not accessible (HTTP $HTTP_CODE)${NC}"
    echo "Please start the API with: cd apps/api && uvicorn main:app --reload"
    exit 1
fi

# === 2. Login ===
echo ""
echo -e "${YELLOW}[2/5] Login...${NC}"
LOGIN_RESPONSE=$(curl -s -X POST "$API_URL/api/auth/login" \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"$TEST_EMAIL\",\"password\":\"$TEST_PASSWORD\"}" \
  -w "\n%{http_code}")

HTTP_CODE=$(echo "$LOGIN_RESPONSE" | tail -n1)
RESPONSE_BODY=$(echo "$LOGIN_RESPONSE" | head -n -1)

if [ "$HTTP_CODE" = "200" ]; then
    TOKEN=$(echo "$RESPONSE_BODY" | grep -o '"access_token":"[^"]*"' | cut -d'"' -f4)
    if [ -n "$TOKEN" ]; then
        echo -e "${GREEN}✅ Login successful${NC}"
        echo "Token: ${TOKEN:0:20}..."
    else
        echo -e "${RED}❌ No token in response${NC}"
        echo "$RESPONSE_BODY"
        exit 1
    fi
else
    echo -e "${RED}❌ Login failed (HTTP $HTTP_CODE)${NC}"
    echo "$RESPONSE_BODY"
    echo ""
    echo "⚠️  Make sure you have a test user. Create one with:"
    echo "   POST $API_URL/api/auth/register"
    exit 1
fi

# === 3. GET /api/lunar-returns/current/report ===
echo ""
echo -e "${YELLOW}[3/5] GET /api/lunar-returns/current/report...${NC}"
REPORT_RESPONSE=$(curl -s -X GET "$API_URL/api/lunar-returns/current/report" \
  -H "Authorization: Bearer $TOKEN" \
  -w "\n%{http_code}")

HTTP_CODE=$(echo "$REPORT_RESPONSE" | tail -n1)
RESPONSE_BODY=$(echo "$REPORT_RESPONSE" | head -n -1)

if [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ Current report retrieved${NC}"

    # Vérifier présence metadata
    if echo "$RESPONSE_BODY" | grep -q '"metadata"'; then
        SOURCE=$(echo "$RESPONSE_BODY" | grep -o '"source":"[^"]*"' | cut -d'"' -f4)
        MODEL=$(echo "$RESPONSE_BODY" | grep -o '"model_used":"[^"]*"' | cut -d'"' -f4)
        echo "   Source: $SOURCE"
        echo "   Model: $MODEL"
    else
        echo -e "${RED}⚠️  No metadata in response${NC}"
    fi
elif [ "$HTTP_CODE" = "404" ]; then
    echo -e "${YELLOW}⚠️  No lunar return found (HTTP 404)${NC}"
    echo "   Create a natal chart first: POST $API_URL/api/natal-chart"
else
    echo -e "${RED}❌ Request failed (HTTP $HTTP_CODE)${NC}"
    echo "$RESPONSE_BODY"
fi

# === 4. POST /api/lunar/interpretation/regenerate ===
echo ""
echo -e "${YELLOW}[4/5] POST /api/lunar/interpretation/regenerate...${NC}"

# D'abord, récupérer un lunar_return_id depuis le rapport
LUNAR_RETURN_ID=$(echo "$RESPONSE_BODY" | grep -o '"lunar_return_id":[0-9]*' | head -1 | cut -d':' -f2)

if [ -z "$LUNAR_RETURN_ID" ] || [ "$LUNAR_RETURN_ID" = "" ]; then
    echo -e "${YELLOW}⚠️  Skipping regenerate test (no lunar_return_id available)${NC}"
else
    REGENERATE_RESPONSE=$(curl -s -X POST "$API_URL/api/lunar/interpretation/regenerate" \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type: application/json" \
      -d "{\"lunar_return_id\":$LUNAR_RETURN_ID,\"subject\":\"full\"}" \
      -w "\n%{http_code}")

    HTTP_CODE=$(echo "$REGENERATE_RESPONSE" | tail -n1)
    RESPONSE_BODY=$(echo "$REGENERATE_RESPONSE" | head -n -1)

    if [ "$HTTP_CODE" = "201" ]; then
        echo -e "${GREEN}✅ Interpretation regenerated${NC}"

        # Vérifier présence forced flag
        if echo "$RESPONSE_BODY" | grep -q '"forced":true'; then
            echo "   Forced: true ✓"
        fi
    else
        echo -e "${RED}❌ Regenerate failed (HTTP $HTTP_CODE)${NC}"
        echo "$RESPONSE_BODY"
    fi
fi

# === 5. GET /api/lunar/interpretation/metadata ===
echo ""
echo -e "${YELLOW}[5/5] GET /api/lunar/interpretation/metadata...${NC}"
METADATA_RESPONSE=$(curl -s -X GET "$API_URL/api/lunar/interpretation/metadata" \
  -H "Authorization: Bearer $TOKEN" \
  -w "\n%{http_code}")

HTTP_CODE=$(echo "$METADATA_RESPONSE" | tail -n1)
RESPONSE_BODY=$(echo "$METADATA_RESPONSE" | head -n -1)

if [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ Metadata retrieved${NC}"

    # Extraire stats
    TOTAL=$(echo "$RESPONSE_BODY" | grep -o '"total_interpretations":[0-9]*' | cut -d':' -f2)
    CACHED_RATE=$(echo "$RESPONSE_BODY" | grep -o '"cached_rate":[0-9.]*' | cut -d':' -f2)

    echo "   Total interpretations: $TOTAL"
    echo "   Cached rate: $CACHED_RATE%"
else
    echo -e "${RED}❌ Metadata request failed (HTTP $HTTP_CODE)${NC}"
    echo "$RESPONSE_BODY"
fi

# === Résumé ===
echo ""
echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}✅ Tests terminés${NC}"
echo -e "${GREEN}================================${NC}"
echo ""
echo "📚 Documentation complète: docs/API_LUNAR_V2.md"
echo ""
