-- Migration: Add dev_external_id column to users table for deterministic DEV_AUTH_BYPASS
-- Date: 2026-01-01
-- Purpose: Allow stable user resolution in development mode using X-Dev-User-Id header

-- Add dev_external_id column (nullable TEXT with unique constraint)
ALTER TABLE users
ADD COLUMN IF NOT EXISTS dev_external_id TEXT UNIQUE;

-- Create index for faster lookups
CREATE INDEX IF NOT EXISTS idx_users_dev_external_id ON users(dev_external_id);

-- Comment explaining the column purpose
COMMENT ON COLUMN users.dev_external_id IS 'External ID for development bypass mode (DEV_AUTH_BYPASS). Used to resolve users deterministically via X-Dev-User-Id header.';
