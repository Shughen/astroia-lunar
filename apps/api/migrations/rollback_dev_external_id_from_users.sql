-- Rollback: Remove dev_external_id column from users table
-- Date: 2026-01-01

-- Drop index first
DROP INDEX IF EXISTS idx_users_dev_external_id;

-- Drop column
ALTER TABLE users
DROP COLUMN IF EXISTS dev_external_id;
