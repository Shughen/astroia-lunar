#!/usr/bin/env zsh

# Script pour inspecter le schéma réel de la table natal_charts
# Usage: ./scripts/inspect_db_schema.sh
#
# Vérifie également users.id pour confirmer le type (doit être INTEGER)

# Charger les variables d'environnement depuis .env
if [ -f .env ]; then
  export $(cat .env | grep -v '^#' | xargs)
fi

if [ -z $DATABASE_URL ]; then
  echo '❌ DATABASE_URL non définie dans .env' >&2
  exit 1
fi

# Extraire les infos de connexion (format: postgresql://user:pass@host:port/dbname)
DB_URL=$DATABASE_URL

# Afficher la requête SQL (pour copier-coller dans Supabase si besoin)
echo '📊 Requête SQL pour natal_charts:'
echo ''
echo 'SELECT'
echo '    column_name,'
echo '    data_type,'
echo '    is_nullable,'
echo '    column_default'
echo 'FROM information_schema.columns'
echo "WHERE table_schema = 'public'"
echo "  AND table_name = 'natal_charts'"
echo 'ORDER BY ordinal_position;'
echo ''

echo '📊 Requête SQL pour users.id (vérification):'
echo ''
echo 'SELECT'
echo '    column_name,'
echo '    data_type'
echo 'FROM information_schema.columns'
echo "WHERE table_schema = 'public'"
echo "  AND table_name = 'users'"
echo "  AND column_name = 'id';"
echo ''

# Essayer via psql si disponible
if command -v psql > /dev/null 2>&1; then
  echo '🔍 Exécution via psql...'
  echo ''
  echo 'Table natal_charts:'
  psql $DB_URL -c "
    SELECT 
        column_name,
        data_type,
        is_nullable,
        COALESCE(column_default, 'NULL') as column_default
    FROM information_schema.columns
    WHERE table_schema = 'public' 
      AND table_name = 'natal_charts'
    ORDER BY ordinal_position;
  " 2>&1
  
  echo ''
  echo 'Vérification users.id (doit être integer):'
  psql $DB_URL -c "
    SELECT 
        column_name,
        data_type
    FROM information_schema.columns
    WHERE table_schema = 'public' 
      AND table_name = 'users'
      AND column_name = 'id';
  " 2>&1
else
  echo '⚠️  psql non disponible - utilisez les requêtes SQL ci-dessus dans Supabase Dashboard'
  exit 1
fi

