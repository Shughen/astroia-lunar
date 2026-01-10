.PHONY: api mobile test seed health install clean help

# Variables
API_DIR = apps/api
MOBILE_DIR = apps/mobile
PYTHON = python3
VENV = $(API_DIR)/.venv

help: ## Affiche cette aide
	@echo "🌙 Astroia Lunar - Commandes Make"
	@echo "================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Installe toutes les dépendances (backend + mobile)
	@echo "📦 Installation des dépendances..."
	@cd $(API_DIR) && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
	@cd $(MOBILE_DIR) && npm install --legacy-peer-deps
	@echo "✅ Dépendances installées"

api: ## Lance le backend FastAPI
	@echo "🚀 Lancement de l'API..."
	@cd $(API_DIR) && source .venv/bin/activate && uvicorn main:app --reload

mobile: ## Lance l'app mobile Expo
	@echo "📱 Lancement de l'app mobile..."
	@cd $(MOBILE_DIR) && npx expo start

test: ## Lance tous les tests
	@echo "🧪 Lancement des tests backend..."
	@cd $(API_DIR) && source .venv/bin/activate && pytest -q
	@echo ""
	@echo "🧪 Lancement des tests mobile..."
	@cd $(MOBILE_DIR) && npm test

test-backend: ## Lance uniquement les tests backend
	@cd $(API_DIR) && source .venv/bin/activate && pytest -v

test-mobile: ## Lance uniquement les tests mobile
	@cd $(MOBILE_DIR) && npm test

seed: ## Lance le script de seed demo
	@echo "🌱 Seed des données de démo..."
	@cd $(API_DIR) && source .venv/bin/activate && python scripts/seed_lunar_demo.py

health: ## Vérifie le health de l'API
	@echo "🏥 Health Check..."
	@curl -s http://localhost:8000/health | jq '.' || echo "❌ API non accessible"

smoke: ## Lance les smoke tests
	@echo "💨 Smoke Tests..."
	@bash scripts/smoke-test.sh

e2e-auth: ## Lance les tests E2E d'authentification
	@echo "🧪 Tests E2E Auth..."
	@cd $(API_DIR) && source .venv/bin/activate && python ../../scripts/e2e_auth.py

db-migrate: ## Applique les migrations Alembic
	@echo "🗄️  Application des migrations..."
	@cd $(API_DIR) && source .venv/bin/activate && alembic upgrade head

db-revision: ## Crée une nouvelle migration
	@echo "🗄️  Création d'une migration..."
	@cd $(API_DIR) && source .venv/bin/activate && alembic revision --autogenerate -m "$(msg)"

clean: ## Nettoie les fichiers temporaires
	@echo "🧹 Nettoyage..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@echo "✅ Nettoyage terminé"

dev: ## Lance API + Mobile en parallèle (tmux requis)
	@echo "🚀 Lancement complet (API + Mobile)..."
	@tmux new-session -d -s astroia "cd $(API_DIR) && source .venv/bin/activate && uvicorn main:app --reload"
	@tmux split-window -v -t astroia "cd $(MOBILE_DIR) && npx expo start"
	@tmux attach -t astroia

stop: ## Arrête tous les processus (API + Mobile)
	@echo "🛑 Arrêt des processus..."
	@lsof -ti:8000 | xargs kill -9 2>/dev/null || echo "API non lancée"
	@pkill -f "expo start" 2>/dev/null || echo "Mobile non lancé"
	@echo "✅ Processus arrêtés"

